from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import re
import requests

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('DA', 'Data Analysis'),
        ('ML', 'Machine Learning'),
        ('DV', 'Data Visualization'),
        ('ST', 'Statistical Analysis'),
        ('DP', 'Data Processing')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    github_link = models.URLField(blank=True, help_text='GitHub repository URL')
    live_demo_link = models.URLField(blank=True)

    def clean_github_link(self):
        """
        Validate GitHub repository URL
        """
        if not self.github_link:
            return

        # Validate URL format
        github_pattern = r'^https?://github\.com/[\w-]+/[\w.-]+/?$'
        if not re.match(github_pattern, self.github_link):
            raise ValidationError({
                'github_link': "Invalid GitHub repository URL. Use format: https://github.com/username/repository"
            })

        try:
            # Extract owner and repo from GitHub URL
            parts = self.github_link.rstrip('/').split('/')
            owner, repo = parts[-2], parts[-1]
            
            # Fetch repository details
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}')
            
            # Check if repository exists
            if response.status_code != 200:
                raise ValidationError({
                    'github_link': f"GitHub repository not found: {self.github_link}"
                })
            
            # Optionally update project details from GitHub
            repo_data = response.json()
            if not self.description and repo_data.get('description'):
                self.description = repo_data['description']
            if not self.title and repo_data.get('name'):
                self.title = repo_data['name']

        except requests.RequestException:
            raise ValidationError({
                'github_link': "Unable to validate GitHub repository. Check your internet connection."
            })

    def clean(self):
        """
        Perform model-wide validation
        """
        super().clean()
        if self.github_link:
            self.clean_github_link()

    def save(self, *args, **kwargs):
        """
        Ensure validation before saving
        """
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Visualization(models.Model):
    TYPE_CHOICES = [
        ('PLT', 'Plot'),
        ('CHT', 'Chart'),
        ('GRF', 'Graph'),
        ('MAP', 'Map'),
        ('DBD', 'Dashboard')
    ]
    image = models.ImageField(upload_to='visualizations/')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='visualizations')
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='visualizations/')
    created_date = models.DateTimeField(default=timezone.now)
    code_snippet = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.project.title}"

class Dataset(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='datasets')
    name = models.CharField(max_length=200)
    description = models.TextField()
    source = models.CharField(max_length=200)
    date_collected = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='datasets/', default='datasets/default.csv',
    help_text='Upload CSV files only')
    rows = models.IntegerField(default=0, editable=False)
    columns = models.IntegerField(default=0, editable=False)
    column_names = models.JSONField(default=list, blank=True)
    sample_data = models.JSONField(default=list, blank=True)
    
    def save(self, *args, **kwargs):
        if self.file:
            try:
                import pandas as pd
                df = pd.read_csv(self.file.path)
                self.rows = len(df)
                self.columns = len(df.columns)
                self.column_names = list(df.columns)
                # Store first 5 rows as sample data
                self.sample_data = df.head().to_dict('records')
            except Exception as e:
                # If there's an error reading the CSV, we'll still save the file
                # but won't update the metadata
                pass
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} - {self.project.title}"
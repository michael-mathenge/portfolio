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

    def save(self, *args, **kwargs):
        """
        Ensure validation before saving
        """
        super().save(*args, **kwargs)
        if self.github_link:
            from .tasks import validate_github_link_task
            validate_github_link_task.delay(self.id)

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
        super().save(*args, **kwargs)
        if self.file:
            from .tasks import process_csv_file_task
            process_csv_file_task.delay(self.id)
    
    def __str__(self):
        return f"{self.name} - {self.project.title}"
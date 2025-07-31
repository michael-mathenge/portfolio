from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    typed_items = models.CharField(max_length=500, help_text="Comma-separated list of items to be typed.")
    
    def __str__(self):
        return self.title

class SocialLink(models.Model):
    hero_section = models.ForeignKey(HeroSection, on_delete=models.CASCADE, related_name='social_links')
    url = models.URLField()
    icon = models.CharField(max_length=100, help_text="e.g., 'bi bi-linkedin'")

    def __str__(self):
        return self.url

class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/')
    birthday = models.CharField(max_length=100)
    website = models.URLField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance_status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name

class ResumeItem(models.Model):
    CATEGORY_CHOICES = [
        ('summary', 'Summary'),
        ('education', 'Education'),
        ('experience', 'Professional Experience'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    period = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.get_category_display()}: {self.title}"

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="e.g., 'bi bi-graph-up-arrow'")

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='testimonials/')
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.author

class ContactInfo(models.Model):
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    whatsapp_number = models.CharField(max_length=20, help_text="Include country code, e.g., +1234567890")

    def __str__(self):
        return "Contact Information"
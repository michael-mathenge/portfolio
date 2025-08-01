# Generated by Django 5.2.1 on 2025-07-12 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('profile_image', models.ImageField(upload_to='profile_images/')),
                ('birthday', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('phone', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('freelance_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp_number', models.CharField(help_text='Include country code, e.g., +1234567890', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('typed_items', models.CharField(help_text='Comma-separated list of items to be typed.', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('summary', 'Summary'), ('education', 'Education'), ('experience', 'Professional Experience')], max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('period', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('icon', models.CharField(help_text="e.g., 'bi bi-graph-up-arrow'", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('author_title', models.CharField(max_length=100)),
                ('author_image', models.ImageField(upload_to='testimonials/')),
                ('rating', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('icon', models.CharField(help_text="e.g., 'bi bi-linkedin'", max_length=100)),
                ('hero_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='portfolio.herosection')),
            ],
        ),
    ]

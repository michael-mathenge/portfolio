# portfolio/views.py
from django.shortcuts import render
import json

from .models import (
    HeroSection, AboutSection, Skill, ResumeItem, Service, Testimonial, ContactInfo
)
from datascience.models import Project as DS_Project

def index(request):
    skills = Skill.objects.all()
    half_skills = len(skills) // 2

    context = {
        'hero_section': HeroSection.objects.first(),
        'about_section': AboutSection.objects.first(),
        'skills_col1': skills[:half_skills],
        'skills_col2': skills[half_skills:],
        'resume_summary': ResumeItem.objects.filter(category='summary').first(),
        'education_items': ResumeItem.objects.filter(category='education'),
        'experience_items': ResumeItem.objects.filter(category='experience'),
        'portfolio_projects': DS_Project.objects.all(),
        'services': Service.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'contact_info': ContactInfo.objects.first(),
    }
    return render(request, 'portfolio/index.html', context)


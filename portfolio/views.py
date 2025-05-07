# portfolio/views.py
from django.shortcuts import render
import json

# request -> response
# request handler

# pull data from a db
# process/ transform data
# send email
# return response



def index(request):
    context = {
        'hero_title': 'Michael Mathenge',
        'typed_items': 'Scrum Master, Data Scientist, Agile Coach',
        'typed_default': 'Scrum Master',
        'social_links': [
            {'url': 'https://linkedin.com/in/michaelmathenge', 'icon': 'bi bi-linkedin'},
            {'url': 'https://twitter.com/michaelmathenge', 'icon': 'bi bi-twitter-x'},
            {'url': 'https://github.com/michaelmathenge', 'icon': 'bi bi-github'}
        ],
        'about_title': 'Scrum Master & Data Science Specialist in Banking',
        'about_description': 'Driving digital transformation through data-driven agile methodologies in the financial sector.',
        'skills': json.dumps([
            {'name': 'Agile Methodologies', 'level': 95},
            {'name': 'Data Science', 'level': 90},
            {'name': 'Financial Analytics', 'level': 85},
            {'name': 'Python', 'level': 90},
            {'name': 'Machine Learning', 'level': 85},
            {'name': 'SQL', 'level': 88}
        ]),

        # Portfolio Section
        'portfolio_description': 'Showcasing my latest projects and professional work',
        'projects': [
            {
                'title': 'Machine Learning Predictor',
                'description': 'Advanced predictive modeling solution',
                'category': 'ml',
                'technologies': ['Python', 'scikit-learn', 'TensorFlow'],
                'image': '/static/img/portfolio/ml-project.jpg',
                'github_link': 'https://github.com/username/ml-project',
                'live_link': None
            },
            {
                'title': 'Web Analytics Dashboard',
                'description': 'Real-time web traffic analysis tool',
                'category': 'web',
                'technologies': ['Django', 'React', 'Chart.js'],
                'image': '/static/img/portfolio/web-analytics.jpg',
                'github_link': 'https://github.com/username/web-analytics',
                'live_link': 'https://webanalytics.example.com'
            }
        ],

        # Services Section
        'services_description': 'Professional services tailored to your needs',
        'services': [
            {
                'title': 'Data Science Consulting',
                'description': 'Custom machine learning and data analysis solutions',
                'icon': 'bi bi-graph-up-arrow'
            },
            {
                'title': 'Web Development',
                'description': 'Full-stack web application development',
                'icon': 'bi bi-code-slash'
            },
            {
                'title': 'AI Model Development',
                'description': 'Building intelligent systems and predictive models',
                'icon': 'bi bi-robot'
            }
        ],

        # Contact Section
        'contact_description': 'Have a project in mind? Let\'s collaborate!',
        'contact_email': 'michael.mathenge@example.com',
        'contact_phone': '+254 (123) 456-7890'
    }
    return render(request, 'portfolio/sections/index.html', context)

def about(request):
    context = {
        'about_title': 'Scrum Master & Data Science Specialist in Banking',
        'about_description': 'Driving digital transformation through data-driven agile methodologies in the financial sector.',
        'skills': json.dumps([
            {'name': 'Agile Methodologies', 'level': 95},
            {'name': 'Data Science', 'level': 90},
            {'name': 'Financial Analytics', 'level': 85},
            {'name': 'Python', 'level': 90},
            {'name': 'Machine Learning', 'level': 85},
            {'name': 'SQL', 'level': 88}
        ])
    }
    return render(request, 'portfolio/about.html', context)

def resume(request):
    context = {
        'resume_description': 'Professional journey and key achievements',
        'work_experience': [
            {
                'title': 'Senior Data Scientist',
                'company': 'Financial Innovation Bank',
                'period': '2021 - Present',
                'description': 'Leading data-driven transformation in banking operations'
            },
            {
                'title': 'Agile Coach',
                'company': 'Tech Innovations Inc.',
                'period': '2018 - 2021',
                'description': 'Implementing agile methodologies across multiple teams'
            }
        ],
        'education': [
            {
                'degree': 'Master of Science in Data Science',
                'institution': 'Tech University',
                'period': '2016 - 2018'
            }
        ]
    }
    return render(request, 'portfolio/resume.html', context)


def portfolio(request):
    context = {
        'portfolio_description': 'Showcasing my latest projects and professional work',
        'projects': [
            {
                'title': 'Machine Learning Predictor',
                'description': 'Advanced predictive modeling solution',
                'category': 'ml',
                'technologies': ['Python', 'scikit-learn', 'TensorFlow'],
                'image': '/static/img/portfolio/ml-project.jpg',
                'github_link': 'https://github.com/username/ml-project',
                'live_link': None
            },
            {
                'title': 'Web Analytics Dashboard',
                'description': 'Real-time web traffic analysis tool',
                'category': 'web',
                'technologies': ['Django', 'React', 'Chart.js'],
                'image': '/static/img/portfolio/web-analytics.jpg',
                'github_link': 'https://github.com/username/web-analytics',
                'live_link': 'https://webanalytics.example.com'
            }
        ]
    }
    return render(request, 'portfolio/portfolio.html', context)

def services(request):
    context = {
        'services_description': 'Professional services tailored to your needs',
        'services': [
            {
                'title': 'Data Science Consulting',
                'description': 'Custom machine learning and data analysis solutions',
                'icon': 'bi bi-graph-up-arrow'
            },
            {
                'title': 'Web Development',
                'description': 'Full-stack web application development',
                'icon': 'bi bi-code-slash'
            },
            {
                'title': 'AI Model Development',
                'description': 'Building intelligent systems and predictive models',
                'icon': 'bi bi-robot'
            }
        ]
    }
    return render(request, 'portfolio/services.html', context)

def contact(request):
    context = {
        'contact_description': 'Get in touch with me',
        'contact_email': 'michael.mathenge@example.com',
        'contact_phone': '+254 (123) 456-7890'
    }
    return render(request, 'portfolio/contact.html', context)


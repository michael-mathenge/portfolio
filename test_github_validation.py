import os
import sys
import django
from django.core.exceptions import ValidationError

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

from datascience.models import Project

def interactive_github_validation_test():
    print("GitHub Repository Link Validation Test")
    print("-------------------------------------")
    
    while True:
        github_link = input("\nEnter a GitHub repository URL (or 'q' to quit): ").strip()
        
        if github_link.lower() == 'q':
            break
        
        project = Project(
            title="Test Project",
            description="Test Description",
            category="DA",
            github_link=github_link
        )
        
        try:
            project.full_clean()
            print(f" Validation Passed for {github_link}")
            
            # Display additional details if populated
            print("\nRepository Details:")
            print(f"Title: {project.title}")
            print(f"Description: {project.description}")
        
        except ValidationError as e:
            print(f" Validation Failed: {e}")

if __name__ == "__main__":
    interactive_github_validation_test()

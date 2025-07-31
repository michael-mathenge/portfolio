from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
import pandas as pd
import logging
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

@shared_task
def validate_github_link_task(project_id):
    from .models import Project
    logger.info(f"Starting GitHub validation for project {project_id}")
    try:
        project = Project.objects.get(id=project_id)
        if project.github_link:
            github_pattern = r'^https?://github\.com/[\w-]+/[\w.-]+/?$'
            if not re.match(github_pattern, project.github_link):
                logger.warning(f"Invalid GitHub URL format for project {project_id}: {project.github_link}")
                return

            parts = project.github_link.rstrip('/').split('/')
            owner, repo = parts[-2], parts[-1]
            
            response = requests.get(f'https://api.github.com/repos/{owner}/{repo}')
            
            if response.status_code != 200:
                logger.error(f"GitHub repository not found for project {project_id}: {project.github_link}")
                return
            
            repo_data = response.json()
            if not project.description and repo_data.get('description'):
                project.description = repo_data['description']
            if not project.title and repo_data.get('name'):
                project.title = repo_data['name']
            project.save()
            logger.info(f"Successfully validated and updated project {project_id} from GitHub.")

    except Project.DoesNotExist:
        logger.error(f"Project with id {project_id} not found for GitHub validation.")
    except requests.RequestException as e:
        logger.error(f"Network error during GitHub validation for project {project_id}: {e}")

@shared_task
def process_csv_file_task(dataset_id):
    from .models import Dataset
    logger.info(f"Starting CSV processing for dataset {dataset_id}")
    try:
        dataset = Dataset.objects.get(id=dataset_id)
        if dataset.file:
            df = pd.read_csv(dataset.file.path)
            dataset.rows = len(df)
            dataset.columns = len(df.columns)
            dataset.column_names = list(df.columns)
            dataset.sample_data = df.head().to_dict('records')
            dataset.save()
            logger.info(f"Successfully processed CSV for dataset {dataset_id}.")
    except Dataset.DoesNotExist:
        logger.error(f"Dataset with id {dataset_id} not found for CSV processing.")
    except Exception as e:
        logger.error(f"Error processing CSV for dataset {dataset_id}: {e}")

# You would also add the image optimization task here
# For example:
#
# from PIL import Image
# import os
# from django.conf import settings
#
# @shared_task
# def optimize_image_task(visualization_id):
#     from .models import Visualization
#     try:
#         visualization = Visualization.objects.get(id=visualization_id)
#         if visualization.image:
#             img_path = visualization.image.path
#             img = Image.open(img_path)
#
#             # Example optimization: resize and save with lower quality
#             img.thumbnail((1024, 1024))
#             optimized_path = os.path.join(settings.MEDIA_ROOT, 'visualizations_optimized')
#             if not os.path.exists(optimized_path):
#                 os.makedirs(optimized_path)
#             
#             filename = os.path.basename(img_path)
#             new_path = os.path.join(optimized_path, filename)
#             img.save(new_path, 'JPEG', quality=85)
#
#             # You might want to save the new path to the model
#             # visualization.optimized_image_path = new_path
#             # visualization.save()
#
#     except Visualization.DoesNotExist:
#         pass
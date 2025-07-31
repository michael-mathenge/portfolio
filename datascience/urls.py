from django.urls import path
from . import views

app_name = 'datascience'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]
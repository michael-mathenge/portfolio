from django.contrib import admin
from .models import Project, Visualization, Dataset

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_date', 'updated_date')
    list_filter = ('category', 'created_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_date'

@admin.register(Visualization)
class VisualizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'type', 'created_date')
    list_filter = ('type', 'project', 'created_date')
    search_fields = ('title', 'description', 'project__title')
    date_hierarchy = 'created_date'

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'source', 'date_collected', 'rows', 'columns')
    list_filter = ('project', 'date_collected')
    search_fields = ('name', 'description', 'project__title')
    date_hierarchy = 'date_collected'
    readonly_fields = ('rows', 'columns', 'column_names', 'sample_data')
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            (None, {
                'fields': ('project', 'name', 'description', 'source', 'date_collected', 'file')
            }),
        ]
        if obj:  # Only show these fields when editing an existing object
            fieldsets.append(
                ('CSV Information', {
                    'fields': ('rows', 'columns', 'column_names', 'sample_data'),
                    'classes': ('collapse',)
                })
            )
        return fieldsets

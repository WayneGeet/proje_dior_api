from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Project  # Import your model


@admin.register(Project)
class Project(LeafletGeoAdmin):
    list_display = ('name', 'location', 'budget',
                    'start_date', 'phase', 'user')

from django.contrib import admin
from .models import DiabetesPrediction  # Import your model here


@admin.register(DiabetesPrediction)
class DiabetesPredictionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'age')
    list_filter = ('gender',)
    search_fields = ('first_name', 'last_name', 'email')

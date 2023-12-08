from django.contrib import admin
from .models import CovidData

# Register the CovidDetection model with the admin site
@admin.register(CovidData)
class CovidDetectionAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_no', 'email', 'gender', 'age', 'chest_scan']
    list_filter = ['gender']
    search_fields = ['first_name', 'last_name', 'phone_no', 'email']


from django.contrib import admin
from .models import LungCancer

@admin.register(LungCancer)
class LungCancerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_no', 'email', 'gender', 'age', 'ct_scan')

from django.urls import path
from . import views

urlpatterns = [
    path('detection', views.brain_tumor_evaluation, name='brain_tumor_evaluation'),
    path('result',views.result, name='result'),
    # Add any other URL patterns you need
]

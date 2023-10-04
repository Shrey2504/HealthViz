from Heart import views
from django.urls import path
urlpatterns = [
    path('detection',views.heart_disease_detection)
]

from BrainTumor import views
from django.urls import path
urlpatterns = [
    path('detection',views.brain)
]

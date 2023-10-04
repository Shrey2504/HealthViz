from Diabetes import views
from django.urls import path
urlpatterns = [
    path('detection',views.save_diabetes_prediction, name='save_diabetes_prediction'),
]

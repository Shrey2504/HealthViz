from Diabetes import views
from django.urls import path
urlpatterns = [
    path('detection',views.diabetes_form, name='diabetes_detection'),
     path('result/<int:prediction_result>/', views.result, name='result'), 
]

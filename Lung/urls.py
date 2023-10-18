from Lung import views
from django.urls import path
urlpatterns = [
    path('detection',views.lung_cancer_detection,name='lungcancer_detection'),
    path('result',views.result,name='result'),
]

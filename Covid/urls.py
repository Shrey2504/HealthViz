from Covid import views
from django.urls import path

urlpatterns = [
    path('detection', views.covid_detection, name='store_covid_data'),
    path('result',views.result, name='store_result'),
]

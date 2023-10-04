from Covid import views
from django.urls import path

urlpatterns = [
    path('detection', views.store_covid_data, name='store_covid_data'),
    path('covid_result/<int:id>/', views.predict_covid, name='covid_result'),
]

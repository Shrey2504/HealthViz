from Home import views
from django.contrib.auth.views import LogoutView
from django.urls import path
urlpatterns = [
    path('',views.home),
    path('index.html',views.home),
    path('diagnosis.html', views.diagnosis),
    path('about.html', views.about),
    path('login.html', views.signin,name='login'),
    path('signup.html', views.signup,name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

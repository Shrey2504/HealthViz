from django.conf import settings
from django.shortcuts import render, redirect

def covid_detection(request):
    return render(request, 'covid/covid.html')
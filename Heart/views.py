from django.shortcuts import render

def heart_disease_detection(request):
    return render(request, 'heart/heart.html')


# Create your views here.

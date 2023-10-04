from django.shortcuts import render

# Create your views here.
def brain(request):
    return render(request, 'brain/brain.html')
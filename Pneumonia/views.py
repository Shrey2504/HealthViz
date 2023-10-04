from django.shortcuts import render

def pneumonia(request):
    return render(request, 'pneumonia/pneumonia.html')
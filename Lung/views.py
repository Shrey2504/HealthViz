from django.shortcuts import render

def lung(request):
    return render(request, 'lung/lung.html')
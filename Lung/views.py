from django.shortcuts import render, redirect
from .models import LungCancer
from .forms import LungCancerDetectionForm


def lung_cancer_detection(request):
    print('Hello')
    if request.method == 'POST':
        form = LungCancerDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            print('saving')
            form.save()  # Save the data to the database
            return redirect('result')  # Redirect to a success page
    else:
        form = LungCancerDetectionForm()
    
    return render(request, 'Lung/lung.html', {'form': form})

def result(request):
    return render(request, 'Lung/result.html')

import os
import numpy as np
from django.shortcuts import render, redirect
from .models import LungCancer
from .forms import LungCancerDetectionForm
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Get the base directory of your Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path to the model file relative to the base directory
MODEL_FILE = os.path.join(BASE_DIR, 'Lung', 'machinelearning', 'lung.h5')

# Load the lung cancer detection model
model = load_model(MODEL_FILE)

# Define a function to preprocess the image for model prediction
def preprocess_image(img):
    img = img.resize((224, 224))  # Resize the image
    img = np.array(img)  # Convert to a numpy array
    img = img.reshape(1, 224, 224, 3)  # Reshape for model input
    img = img / 255.0  # Normalize pixel values
    return img

def lung_cancer_detection(request):
    if request.method == 'POST':
        form = LungCancerDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            lung_cancer_data = LungCancer(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_no=form.cleaned_data['phone_no'],
                email=form.cleaned_data['email'],
                gender=form.cleaned_data['gender'],
                age=form.cleaned_data['age'],
                ct_scan=form.cleaned_data['ct_scan']
            )
            lung_cancer_data.save()

            # Get the image from the saved data
            uploaded_image = image.load_img(lung_cancer_data.ct_scan.path)

            # Preprocess the image and make a prediction
            preprocessed_image = preprocess_image(uploaded_image)
            prediction = model.predict(preprocessed_image)
            
            # Determine the result based on the prediction
            if prediction[0][0] < 0.5:
                result = 'No Lung Cancer'
            else:
                result = 'Lung Cancer Detected'

            user_data = {
                'first_name': lung_cancer_data.first_name,
                'last_name': lung_cancer_data.last_name,
                'phone_no': lung_cancer_data.phone_no,
                'email': lung_cancer_data.email,
                'gender': lung_cancer_data.gender,
                'age': lung_cancer_data.age,
            }

            return render(request, 'Lung/result.html', {'user_data': user_data, 'result': result})

    else:
        form = LungCancerDetectionForm()

    return render(request, 'Lung/lung.html', {'form': form})

def result(request):
    return render(request, 'Lung/result.html')

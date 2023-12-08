import cv2
import os
from django.shortcuts import render
from .forms import CovidDetectionForm
from .models import CovidData
from tensorflow.keras.models import load_model
import numpy as np


# Get the base directory of your Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path to the model file relative to the base directory
MODEL_FILE = os.path.join(BASE_DIR,'Covid', 'machinelearning', 'covid.h5')

# Load the brain tumor detection model
model = load_model(MODEL_FILE)

# Function to preprocess and predict an image
def predict_covid(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img.reshape(1, 224, 224, 3)
    img = img / 255.0
    pred = model.predict(img)
    return pred[0]

def covid_detection(request):
    if request.method == 'POST':
        form = CovidDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data and save it to the database
            covid_detection = CovidData(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_no=form.cleaned_data['phone_no'],
                email=form.cleaned_data['email'],
                gender=form.cleaned_data['gender'],
                age=form.cleaned_data['age'],
                chest_scan=form.cleaned_data['chest_scan']
            )
            covid_detection.save()

            # Get the path of the uploaded chest scan image
            image_path = covid_detection.chest_scan.path

            # Make a prediction using the model
            pred = predict_covid(image_path)

            # Determine the result based on the prediction threshold (0.5 in this case)
            if pred < 0.5:
                result = 'COVID-19 Detected'
            else:
                result = 'No COVID-19 Detected'

            # Render the result page with user data and prediction result
            user_data = {
                'first_name': covid_detection.first_name,
                'last_name': covid_detection.last_name,
                'phone_no': covid_detection.phone_no,
                'email': covid_detection.email,
                'gender': covid_detection.gender,
                'age': covid_detection.age,
            }

            return render(request, 'covid/result.html', {'user_data': user_data, 'result': result})

    else:
        form = CovidDetectionForm()

    return render(request, 'covid/covid.html', {'form': form})


def result(request):
    return render(request, 'covid/result.html')

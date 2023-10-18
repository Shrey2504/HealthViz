import os
from django.http import HttpResponse
import joblib
from django.conf import settings
from django.shortcuts import render, redirect
from .models import DiabetesPrediction
from .forms import DiabetesDetectionForm

# ... your other imports ...

# Define the path to the diabetes.sav model file
model_path = os.path.join(settings.BASE_DIR, 'Diabetes', 'machinelearning', 'diabetes.sav')

# Load the model using joblib
loaded_model = joblib.load(model_path)

def diabetes_form(request):
    if request.method == 'POST':
        form = DiabetesDetectionForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # Create an instance of the DiabetesPrediction model and populate it with the form data
            instance = DiabetesPrediction(
                first_name=cleaned_data['first_name'],
                last_name=cleaned_data['last_name'],
                phone_no=cleaned_data['phone_no'],
                email=cleaned_data['email'],
                gender=cleaned_data['gender'],
                pregnancies=cleaned_data['pregnancies'],
                glucose=cleaned_data['glucose'],
                blood_pressure=cleaned_data['blood_pressure'],
                skin_thickness=cleaned_data['skin_thickness'],
                insulin=cleaned_data['insulin'],
                bmi=cleaned_data['bmi'],
                diabetes_pedigree=cleaned_data['diabetes_pedigree'],
                age=cleaned_data['age']
            )

            # Save the instance to the database
            instance.save()

            # Prepare the input data to match the features used in the model
            features = ['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'diabetes_pedigree', 'age']
            user_data = [cleaned_data[feature] for feature in features]
            # Make predictions using the loaded model
            prediction_result = loaded_model.predict([user_data])[0]

            # Redirect to the 'result' view with the prediction result as a URL parameter
            return render(request,'diabetes/result.html', {'form': form, 'prediction_result': prediction_result})

    else:
        form = DiabetesDetectionForm()

    return render(request, 'diabetes/diabetes.html', {'form': form})

def result(request):
    # Retrieve the form data and prediction result from session variables
    form_data = request.session.get('form_data', {})
    prediction_result = request.session.get('prediction_result', None)

    if not prediction_result:
        # Handle the case where there is no prediction result
        return HttpResponse("Prediction result not available")

    return render(request, 'diabetes/result.html', {'form_data': form_data, 'prediction_result': prediction_result})
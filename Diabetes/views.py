import joblib
from django.conf import settings
from django.shortcuts import render, redirect
from .models import DiabetesPrediction
from django.contrib import messages
import os

model_path = os.path.join(settings.BASE_DIR, 'Diabetes',
                          'machinelearning', 'diabetes.sav')
loaded_model = joblib.load(model_path)


def save_diabetes_prediction(request):
    # Add this at the beginning of your view function
    print(request.POST)

    if request.method == 'POST':
        # Retrieve form data from POST request
        # Retrieve form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        pregnancies = request.POST.get('pregnancies')
        glucose = request.POST.get('glucose')
        blood_pressure = request.POST.get('blood_pressure')
        skin_thickness = request.POST.get('skin_thickness')
        insulin = request.POST.get('insulin')
        bmi = request.POST.get('bmi')
        diabetes_pedigree = request.POST.get('diabetes_pedigree')
        age = request.POST.get('age')

        input_data = [
            float(pregnancies),
            float(glucose),
            float(blood_pressure),
            float(skin_thickness),
            float(insulin),
            float(bmi),
            float(diabetes_pedigree),
            float(age)
        ]

        # Perform prediction using the loaded model
        prediction = loaded_model.predict([input_data])[0]

        # Optionally, format or round the prediction result
        formatted_prediction = round(prediction, 2)

        # Create and save a new DiabetesPrediction instance
        prediction_instance = DiabetesPrediction(
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            email=email,
            gender=gender,
            pregnancies=pregnancies,
            glucose=glucose,
            blood_pressure=blood_pressure,
            skin_thickness=skin_thickness,
            insulin=insulin,
            bmi=bmi,
            diabetes_pedigree=diabetes_pedigree,
            age=age,
            prediction_result=formatted_prediction  # Save the formatted prediction result
        )
        prediction_instance.save()

        # Optionally, you can show a success message using Django's messages framework
        messages.success(request, 'Data saved successfully. Prediction: {}'.format(
            formatted_prediction))

        # Redirect to a success page or another page
        return redirect('diabetes.html')

    return render(request, 'diabetes/diabetes.html')

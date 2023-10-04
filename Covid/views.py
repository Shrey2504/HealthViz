from django.conf import settings
from django.shortcuts import render, redirect
import os
from .models import CovidDetection
from tensorflow import keras
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

# ... (preprocess_image function remains the same)
def preprocess_image(image_path):
    # Check if image_path is a string or an ImageFieldFile object
    if isinstance(image_path, str):
        # If it's already a string, use it as is
        image_file_path = image_path
    else:
        # If it's an ImageFieldFile, get the path from the object
        image_file_path = image_path.path

    # Load the image using cv2
    image = cv2.imread(r"{}".format(str(image_file_path)))
    # Resize the image to the target dimensions
    target_width, target_height = (224, 224)  # Adjust these dimensions as needed
    image = cv2.resize(image, (target_width, target_height))
    # Convert the image to a numpy array
    image = np.array(image)
    # Normalize pixel values
    image = image / 255.0
    # Reshape the image to match the model's input shape
    image = image.reshape(1, target_width, target_height, 3)
    return image


def store_covid_data(request):
    if request.method == 'POST':
        # Process form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        chest_scan = request.FILES.get('chest_scan')

        # Save form data to the database
        covid_detection = CovidDetection(
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            email=email,
            gender=gender,
            age=age,
            chest_scan=chest_scan
        )
        covid_detection.save()

        # Redirect to the COVID detection result page with the detection ID
        return redirect('covid_result', id=covid_detection.id)

    return render(request, 'covid/covid.html')

def predict_covid(request, id):
    try:
        # Retrieve the COVID detection record by its ID
        covid_detection = CovidDetection.objects.get(pk=id)

        # Load the pre-trained model from the root directory
        model_path = os.path.join(settings.BASE_DIR, 'Covid', 'machinelearning', 'covid.h5')
        model = keras.models.load_model(model_path)

        # Preprocess the input image
        image = preprocess_image(covid_detection.chest_scan)

        if image is not None:
            # Make predictions using the loaded model
            prediction = model.predict(image)
            # Assuming prediction is a binary classification result
            result = "Positive" if prediction[0][0] >= 0.5 else "Negative"
        else:
            result = "Error: Invalid image format"

        return render(request, 'covid/covid_result.html', {'result': result})

    except CovidDetection.DoesNotExist:
        return render(request, 'covid/covid_result.html', {'result': 'Error: Record not found'})
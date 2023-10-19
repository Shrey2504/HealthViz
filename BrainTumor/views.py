import os
from django.shortcuts import render, redirect
from .forms import BrainTumorForm
from .models import BrainTumor

# Import necessary libraries
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
import imutils
import matplotlib.pyplot as plt


# Get the base directory of your Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path to the model file relative to the base directory
MODEL_FILE = os.path.join(BASE_DIR,'BrainTumor', 'machinelearning', 'brain_tumor.h5')

# Load the brain tumor detection model
model = load_model(MODEL_FILE)

IMG_SIZE = (240, 240)
def preprocess_imgs(set_name, img_size):
    """
    Resize and apply VGG-15 preprocessing
    """
    set_new = []
    for img in set_name:
        img = cv2.resize(img,dsize=img_size,interpolation=cv2.INTER_CUBIC)
        set_new.append(preprocess_input(img))
    return np.array(set_new)

def crop_imgs(set_name, add_pixels_value=0):
    """
    Finds the extreme points on the image and crops the rectangular out of them
    """
    set_new = []
    for img in set_name:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        # threshold the image, then perform a series of erosions +
        # dilations to remove any small regions of noise
        thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=2)

        # find contours in thresholded image, then grab the largest one
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key=cv2.contourArea)

        # find the extreme points
        extLeft = tuple(c[c[:, :, 0].argmin()][0])
        extRight = tuple(c[c[:, :, 0].argmax()][0])
        extTop = tuple(c[c[:, :, 1].argmin()][0])
        extBot = tuple(c[c[:, :, 1].argmax()][0])

        ADD_PIXELS = add_pixels_value
        new_img = img[extTop[1]-ADD_PIXELS:extBot[1]+ADD_PIXELS, extLeft[0]-ADD_PIXELS:extRight[0]+ADD_PIXELS].copy()
        set_new.append(new_img)

    return np.array(set_new)

def brain_tumor_evaluation(request):
    if request.method == 'POST':
        form = BrainTumorForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data and save it to the database
            brainTumor = BrainTumor(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_no=form.cleaned_data['phone_no'],
                email=form.cleaned_data['email'],
                gender=form.cleaned_data['gender'],
                age=form.cleaned_data['age'],
                brain_mri=form.cleaned_data['brain_mri']
            )
            brainTumor.save()

            # Preprocess and make a prediction
            img = cv2.imread(brainTumor.brain_mri.path)
            img = crop_imgs([img])
            img = img.reshape(img.shape[1:])
            img = preprocess_imgs([img], IMG_SIZE)

            pred = model.predict(img)

            if pred < 0.5:
                result = 'No Tumor'
            else:
                result = 'Brain has a tumor'

            # Render the result page with user data and result
            user_data = {
                'first_name': brainTumor.first_name,
                'last_name': brainTumor.last_name,
                'phone_no': brainTumor.phone_no,
                'email': brainTumor.email,
                'gender': brainTumor.gender,
                'age': brainTumor.age,
            }

            return render(request, 'brain/result.html', {'user_data': user_data, 'result': result})

    else:
        form = BrainTumorForm()

    return render(request, 'brain/brain.html', {'form': form})


def result(request):
    return render(request, 'brain/result.html')
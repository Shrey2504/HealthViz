from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import SignUp  # Import your SignUp model

# Create your views here.


def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def diagnosis(request):
    return render(request, 'home/diagnosis.html')

def login(request):
    return render(request, 'home/login.html')

def register_view(request):
    return render(request, 'home/signup.html')


def signup(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        medical_info = request.POST.get('medical_info', '')  # Provide a default value

        # Create and save a new SignUp instance
        signup_instance = SignUp(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            email=email,
            medical_info=medical_info
        )
        signup_instance.save()

        return redirect('index.html')  # Redirect to a success page
    return render(request, 'home/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # Authentication failed, you can handle it here (e.g., display an error message)
            pass

    return render(request, 'home/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # Assuming the form field is named 'username'
        password = request.POST['password']  # Assuming the form field is named 'password'

        # Validate login data against SignUp model
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # Invalid login credentials, display an error message
            error_message = "Invalid username or password. Please try again."
    else:
        error_message = ""

    return render(request, 'home/login.html', {'error_message': error_message})
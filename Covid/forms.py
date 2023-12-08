from django import forms

class CovidDetectionForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)
    phone_no = forms.CharField(label='Phone No.', max_length=15, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    gender = forms.ChoiceField(label='Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
    age = forms.IntegerField(label='Age', required=True)
    chest_scan = forms.ImageField(label='Upload Your Chest Scan (Image)', required=True)

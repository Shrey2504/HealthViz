from django import forms

class DiabetesDetectionForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_no = forms.CharField(max_length=15)
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    pregnancies = forms.IntegerField()
    glucose = forms.DecimalField()
    blood_pressure = forms.DecimalField()
    skin_thickness = forms.DecimalField()
    insulin = forms.DecimalField()
    bmi = forms.DecimalField()
    diabetes_pedigree = forms.DecimalField()
    age = forms.IntegerField()

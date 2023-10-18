from django import forms
from .models import LungCancer

class LungCancerDetectionForm(forms.ModelForm):
    class Meta:
        model = LungCancer
        fields = [
            'first_name',
            'last_name',
            'phone_no',
            'email',
            'gender',
            'age',
            'ct_scan',
        ]

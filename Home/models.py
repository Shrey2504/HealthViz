from django.db import models

class SignUp(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    email = models.EmailField()
    medical_info = models.CharField(max_length=255, blank=True, null=True)  # Optional field for medical info

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

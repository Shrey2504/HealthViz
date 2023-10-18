from django.db import models

class LungCancer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)  # Assuming you store it as a string with the country code
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.PositiveIntegerField()
    ct_scan = models.ImageField(upload_to='ct_scans/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

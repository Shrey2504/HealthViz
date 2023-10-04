from django.db import models

class CovidDetection(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.IntegerField()
    chest_scan = models.ImageField(upload_to='chest_scans/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from django.db import models

class CovidData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.IntegerField()
    chest_scan = models.ImageField(upload_to='chest_scans/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

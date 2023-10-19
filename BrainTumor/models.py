from django.db import models

class BrainTumor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.IntegerField()
    brain_mri = models.ImageField(upload_to='brain_mri_images/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from django.db import models

class DiabetesPrediction(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    pregnancies = models.PositiveIntegerField()
    glucose = models.PositiveIntegerField()
    blood_pressure = models.PositiveIntegerField()
    skin_thickness = models.PositiveIntegerField()
    insulin = models.PositiveIntegerField()
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    diabetes_pedigree = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

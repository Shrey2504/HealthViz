# Generated by Django 4.2 on 2023-10-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiabetesPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('pregnancies', models.PositiveIntegerField()),
                ('glucose', models.PositiveIntegerField()),
                ('blood_pressure', models.PositiveIntegerField()),
                ('skin_thickness', models.PositiveIntegerField()),
                ('insulin', models.PositiveIntegerField()),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('diabetes_pedigree', models.DecimalField(decimal_places=2, max_digits=5)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-10-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrainTumor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('age', models.IntegerField()),
                ('brain_mri', models.ImageField(upload_to='brain_mri_images/')),
            ],
        ),
    ]

from django.db import models

# Create your models here.
class registration_model(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=10)
    email=models.EmailField()
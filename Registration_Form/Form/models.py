from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

#Custom Validators
def mobile_number_validator(mobile_number):
    if len(str(mobile_number))>10 or len(str(mobile_number))<10:
        raise ValidationError("Contact is not valid.")

def emailDomainValidator(email):
    username, domain=email.split('@')
    if domain!='gmail.com':
        raise ValidationError("Enter a valid gmail id.")

class registration_model(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    #mobile_number = PhoneNumberField()
    mobile_number=models.IntegerField(validators=[mobile_number_validator])
    email=models.EmailField(unique=True,validators=[emailDomainValidator],error_messages={'unique':'Already Registered!'})
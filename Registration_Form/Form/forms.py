from django import forms

class Registartion_form(forms.Form):
    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    address=forms.CharField(max_length=500)
    mobile_number=forms.CharField(max_length=10)
    password=forms.PasswordInput()
        
    

from django import forms
from .models import registration_model

class Registartion_form(forms.ModelForm):
    class Meta:
        model=registration_model
        fields='__all__'
    
        
    

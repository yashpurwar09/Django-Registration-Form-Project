from django import forms
from .models import registration_model

class Registartion_form(forms.ModelForm):
    class Meta:
        model=registration_model
        fields='__all__'
        widgets={
            'first_name':forms.TextInput(attrs={
              'class':'form-control',  
            }),
            'last_name':forms.TextInput(attrs={
              'class':'form-control',  
            }),
            'address':forms.TextInput(attrs={
              'class':'form-control',  
            }),
            'mobile_number':forms.NumberInput(attrs={
              'class':'form-control',  
            }),
            'email':forms.EmailInput(attrs={
              'class':'form-control',  
            }),
        }
    
        
    

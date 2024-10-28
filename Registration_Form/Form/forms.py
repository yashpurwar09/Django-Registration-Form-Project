from django import forms
from .models import registration_model
from phonenumber_field.widgets import RegionalPhoneNumberWidget

class Registartion_form(forms.ModelForm):
    class Meta:
        model=registration_model
        fields='__all__'
        widgets={
            'first_name':forms.TextInput(attrs={
              'class':'form-control border-success',  
            }),
            'last_name':forms.TextInput(attrs={
              'class':'form-control border-success',  
            }),
            'address':forms.TextInput(attrs={
              'class':'form-control border-success',  
            }),
            ''''mobile_number':forms.NumberInput(attrs={
              'class':'form-control border-success',  
            }),'''
            'mobile_number':RegionalPhoneNumberWidget(region="IN"),
            'email':forms.EmailInput(attrs={
              'class':'form-control border-success',  
            }),
        }
    #mobile number validator
    # def clean_mobile_number(self):
    #     mobile_number=self.cleaned_data['mobile_number']
    #     print(mobile_number)
    #     if len(mobile_number)>10 or len(mobile_number<10):
    #         print(mobile_number)
    #         raise forms.ValidationError("Contact is not valid.")
    #     return mobile_number
    

    
        
    

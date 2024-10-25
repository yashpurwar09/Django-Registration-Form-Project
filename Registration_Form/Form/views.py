from django.shortcuts import render
from .forms import Registartion_form

# Create your views here.

def create_form(request):
    context={
        "form":Registartion_form(),
    }
    return render(request,'form.html',context)

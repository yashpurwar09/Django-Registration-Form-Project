from django.shortcuts import render
from .forms import Registartion_form
from django.core.mail import send_mail

# Create your views here.
def mail(name,email):
    subject="Registration Successful"
    message=f"Hi {name}, You are registered for"
    send_mail(subject=subject,message=message,from_email='yashpurwar08@gmail.com',recipient_list=[email],fail_silently=True)

def create_form(request):
    if request.method=='POST':
        form = Registartion_form(request.POST)
        if form.is_valid():
            name=f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
            email = form.cleaned_data['email']
            form.save()
            mail(name,email)
            return render(request, 'SubmitForm.html')
        else:
            return render(request,'form.html',{'form':form})
    context={
        "form":Registartion_form(),
    }
    return render(request,'form.html',context)

from django.shortcuts import render
from .forms import Registartion_form, OtpForm
from django.core.mail import send_mail
from random import randrange
from django.core.exceptions import ValidationError

# Create your views here.
sixdigitotp=''
def otp_generator():
    sixdigitotp=randrange(100000,999999)
    return sixdigitotp

def otp_check(request):
    if request.method=='POST':
        if request.POST['otp']==str(request.session['generated_otp']):
            form_data=request.session['form']
            form=Registartion_form(form_data)
            form.save()
            return render(request, 'SubmitForm.html')
        else:
            form=OtpForm(request.POST)
            OtpForm.add_error(form,field='otp',error='Incorrect Otp')
            return render(request,'otp.html',{'form':form})
    context={
        'form':OtpForm()
    }
    return render(request,'otp.html',context)

def mail(name,email):
    subject="Registration Successful"
    generate_otp=otp_generator()
    message=f"Hi {name}, OTP is: {generate_otp}"
    send_mail(subject=subject,message=message,from_email='yashpurwar08@gmail.com',recipient_list=[email],fail_silently=True)
    return generate_otp

def create_form(request):
    if request.method=='POST':
        form = Registartion_form(request.POST)
        if form.is_valid():
            name=f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
            email = form.cleaned_data['email']
            generated_otp=mail(name,email)
            request.session['generated_otp']=generated_otp
            request.session['form']=form.cleaned_data
            context={
                'form':OtpForm(),
            }
            return render(request,'otp.html',context)
        else:
            return render(request,'form.html',{'form':form})
    context={
        "form":Registartion_form(),
    }
    return render(request,'form.html',context)

from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_form, name='create_form'),
    path('otp_check', views.otp_check, name='otp_check'),
]

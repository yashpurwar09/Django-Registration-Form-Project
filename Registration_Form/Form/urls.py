from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_form, name='create_form'),
]

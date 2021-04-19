from django.urls import path,include
from . import views

urlpatterns = [
    path('contact-form',views.contact,name='contact'),
]
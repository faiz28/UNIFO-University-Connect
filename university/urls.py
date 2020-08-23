from django.urls import path,include
from . import views

urlpatterns = [
    path('university',views.university,name='university'),
]
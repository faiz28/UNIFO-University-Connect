from django.urls import path,include
from . import views

urlpatterns = [
    path('registration',views.registration,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
]
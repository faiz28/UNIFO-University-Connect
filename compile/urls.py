from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.compiler,name='compilerrrr'),
    path('codeplay/',views.codeplay,name='codeplay'),
   ]
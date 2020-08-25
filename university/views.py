from django.shortcuts import render
from .models import university
# Create your views here.

def university(request):

    return render(request,'university.html')
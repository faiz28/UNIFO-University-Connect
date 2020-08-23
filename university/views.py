from django.shortcuts import render

# Create your views here.

def university(request):
    return render(request,'university.html')
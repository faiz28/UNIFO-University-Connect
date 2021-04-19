from django.shortcuts import render,redirect
from .models import contact_form
# Create your views here.

def contact(request):
    if request.method == 'POST':
      
        p=contact_form.objects.create(name=request.POST.get('name'),gmail=request.POST.get('email'),message=request.POST['message'])
        p.save()
        return redirect('home')
    else:
        return render(request,'contact.html')
     
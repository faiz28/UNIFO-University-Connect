from django.shortcuts import render,redirect,HttpResponseRedirect
from homepage.models import category
from django.db.models import Q
from .models import university_list,uni_cat,department_list,university_name,achievment_list
from account.models import student_data,userinfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import achievement_form
from django.shortcuts import get_object_or_404


# Create your views here.
uni_list=university_list.objects.all()

def publicuniversitylist(request):
    return render(request,'publicuniversitylist.html',{'uni_list':uni_list})

def engineeruniversitylist(request):
    return render(request,'engineeringuniversitylist.html',{'uni_list':uni_list})

def medicaluniversitylist(request):
    return render(request,'medical.html',{'uni_list':uni_list})

def privateuniversitylist(request):
    return render(request,'private.html',{'uni_list':uni_list})

def agriculturaluniversitylist(request):
    return render(request,'agriculter.html',{'uni_list':uni_list})

def stuuniversitylist(request):
    return render(request,'stu.html',{'uni_list':uni_list,'uni_cat':uni_cat})

def suuniversitylist(request):
    return render(request,'su.html',{'uni_list':uni_list,'uni_cat':uni_cat})


def uni_details(request,uni_id):
    uni_info=university_list.objects.filter(Q(id=uni_id)) #collect university information by using university id
    store="" 
    for data in uni_info: 
        store=data.uni_name #university name 

    d_list=department_list.objects.all().filter(uni_name=store) #university all department list collect by using university name
    return render(request,'university-details.html',{'uni_info':uni_info,'department_list':d_list})

def department_deatils(request,dep_id):
    depart_details=department_list.objects.filter(Q(id=dep_id)) #department details information collect
    aciv_list=achievment_list.objects.filter(Q(department_id=dep_id))
    check_user_auth=0
    if request.user.is_authenticated:
        username = request.user.username
        stu_data=student_data.objects.filter(Q(username=username))
        return render(request,'department_deatils.html',{'depart_details':depart_details,'stu_data':stu_data,'dep_id':dep_id,'achiev_list':aciv_list})
    else:
        check_user_auth= -1
        return render(request,'department_deatils.html',{'depart_details':depart_details,'check_user_auth':check_user_auth,'achiev_list':aciv_list,'dep_id':dep_id})

#Achievment Details
def add_achievment(request,dep_id):
    
    if request.method == 'POST':
        form = achievement_form(request.POST, request.FILES)
        if form.is_valid():
            obj=form.save()
            obj.department_id=dep_id
            obj.username=request.user.username
            obj.save()
            next = '/university/'+str(dep_id)+'/department_deatils/' 
            return HttpResponseRedirect(next)
    else:
        form=achievement_form()
    return render(request,'add_achievment.html',{'dep_id':dep_id,'form':form})


def achiv_details(request,acv_id):
    details=achievment_list.objects.filter(Q(id=acv_id)) 
    return render(request,'achievment.html',{'details':details,'acv_id':acv_id})

def update_achievement(request,acv_id):
    instance = get_object_or_404(achievment_list, id=acv_id)
    next='/university/'+str(instance.department_id)+'/department_deatils/'
    if instance:
        instance.delete()
    print(next)
    return HttpResponseRedirect(next)


def event(request):
    return render(request,'create_event.html')

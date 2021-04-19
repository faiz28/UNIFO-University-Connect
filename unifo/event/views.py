from django.shortcuts import render,redirect
from university.models import department_list,subject_list
from .models import event_info
from account.models import student_data
from .forms import event_form
from django.db.models import Q
from university.models import department_list

# Create your views here.
def create(request,dep_id):
    if request.method == 'POST':
        form = event_form(request.POST, request.FILES)
        if form.is_valid():
            obj=form.save()
            obj.username=request.user.username
            obj.department_id=dep_id
            #university search
            data=department_list.objects.filter(Q(id=dep_id))
            uni_name="rr"
            dep_name="dd"
            for uni in data:
                uni_name=uni.uni_name.university_name
                dep=uni.department_name.sub_name
            obj.uni_name= uni_name
            obj.department_name=dep 
            obj.save()
            return redirect('home')
    else:
            form=event_form()
            print("error")
    return render(request,'create_event.html',{'form':form})
def event_view(request,event_id):
    event=event_info.objects.filter(Q(id=event_id)) 
    return render(request,'event_details.html',{'event':event})

def uni_event(request,dep_id):
    event_list=event_info.objects.filter(Q(department_id=dep_id))
    d_name=""
    for data in event_list:
        d_name=data.department_name
    event_list=event_info.objects.filter(Q(department_name=d_name))
    
    check_user_auth=0
    if request.user.is_authenticated:
        username = request.user.username
        stu_data=student_data.objects.filter(Q(username=username))
        return render(request,'university_event.html',{'event_list':event_list,'dep_id':dep_id,'stu_data':stu_data})
    else:
        check_user_auth= -1
        return render(request,'university_event.html',{'event_list':event_list,'dep_id':dep_id})

def All_event(request,dep_id):
    username = request.user.username
    dep_name=""
    stu_data=student_data.objects.filter(Q(username=username))
    for data in stu_data:
        dep_name=data.department_name
    all_event=event_info.objects.filter(Q(department_name=dep_name))
       
    return render(request,'All_university_event.html',{'event_list':all_event})
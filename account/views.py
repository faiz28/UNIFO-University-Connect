from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import student_data,userinfo
from django.db.models import Q
from university.models import subject_list,university_name,achievment_list,department_list
from .forms import user_form


# Create your views here.
def register(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                username=request.POST['username']
                user=User.objects.filter(Q(username=username))
                useremail = request.POST['email']
                email=User.objects.filter(Q(email=useremail))
                if user.count()==1:
                    return render(request,'signup.html',{'error':'Username Already Exists'})
                else:
                    if email.count()==1:
                        return render(request,'signup.html',{'error':'Email Already Exists'})
                    else:
                        user=User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'], first_name=request.POST['first_name'])
                        user.save()
                        usersss=userinfo.objects.create(username=request.POST['username'],fullname=request.POST['first_name'])
                        usersss.save()
                        socialsss=student_data.objects.create(username=request.POST['username'])
                        socialsss.save()
                        auth.login(request,user)
                        return redirect('home')
                    
                
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'], first_name=request.POST['first_name'])
                user.save()
                usersss=userinfo.objects.create(username=request.POST['username'],fullname=request.POST['first_name'])
                usersss.save()
                socialsss=student_data.objects.create(username=request.POST['username'])
                socialsss.save()
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'signup.html',{'error':'Password Does not match'})
    else:
        return render(request,'signup.html')
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def user_profile(request):
    username=request.user.username
    firstname=request.user.first_name
    info=User.objects.filter(Q(username=username))
    usersss=userinfo.objects.filter(Q(username=username))
    stu_data=student_data.objects.filter(Q(username=username))
    user_added=achievment_list.objects.filter(Q(username=request.user.username))
    return render(request,'userprofile.html',{'info':info,'userinfo':usersss,'stu_data':stu_data,'user_added':user_added})

def user_update(request):
    # username=request.user.username
    # email=request.user.email
    # #user information filtering
    # info=User.objects.filter(Q(username=username))
    # usersss=userinfo.objects.filter(Q(username=username))
    # stu_data=student_data.objects.filter(Q(username=username))
    # user_added=achievment_list.objects.filter(Q(username=request.user.username))
    #userinfo forms

    username=request.user.username
    userprofile = userinfo.objects.get(username=username)
    # user=userinfo.objects.filter(Q(username=username))
    form=user_form(instance=userprofile)
    context = {'form': form}




    # subject list collect from database
    # sub_list=subject_list.objects.all()
    # uni_name=university_name.objects.all()

    if request.method == 'POST':
        # check= userinfo.objects.filter(Q(username=username))
        form=user_form(request.POST,request.FILES,instance=userprofile)
        if form.is_valid():
            form.save()
        #  userinfo.objects.filter(username=username).update(fullname=request.POST['fullname'],address=request.POST['address'],mobile_num=request.POST['number'],work=request.POST['work'])
        return render(request,'profileupdate.html',context)
    
    return render(request,'profileupdate.html',context)
    
@login_required
def department_registration(request,dep_id):
    depart_details=department_list.objects.filter(Q(id=dep_id))
    # if request.method == 'POST':
    #     username=request.user.username
    #     student_data.objects.filter(username=username).update(student_id=request.POST['stu_id'],department_id=request.POST['department_id'],uni_name=request.POST['university_name'],department_name=request.POST['department_name'])
    #     return render(request,'department_deatils.html',{'dep_info':dep_info,'dep_id':dep_id})
    
    if request.method == 'POST':
        username=request.user.username
        store=student_data.objects.filter(Q(username=username))
        student_data.objects.filter(username=username).update(student_id=request.POST['stu_id'],department_id=request.POST['dep_id'],uni_name=request.POST['uni_name'],department_name=request.POST['dep_name']) 
        return redirect('home')
    return render(request,'department_registration.html',{'dep_info':depart_details,'dep_id':dep_id})
    
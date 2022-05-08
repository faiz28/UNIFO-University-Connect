from django.shortcuts import render
from accounts.models import student_data
from university.models import department_list
from django.db.models import Q
from event.models import event_info

# Create your views here.


def home(request):
    check_user_auth = 0
    if request.user.is_authenticated:
        username = request.user.username
        stu_data = student_data.objects.filter(Q(username=username))

        dep_id = -1
        dep_name = ""
        for data in stu_data:
            dep_id = data.department_id
            dep_name = data.department_name
        dep_info = department_list.objects.filter(Q(id=dep_id))
        all_event = event_info.objects.filter(Q(department_name=dep_name))
        if len(dep_info) == 0:
            check_user_auth = -1
        return render(request, 'home.html', {'dep_info': dep_info, 'all_event': all_event, 'check_user_auth': check_user_auth})
    else:
        check_user_auth = -1
        return render(request, 'home.html', {'check_user_auth': check_user_auth})

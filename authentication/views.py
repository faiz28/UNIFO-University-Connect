from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from helpers.decorators import auth_user_should_not_access
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import threading
from django.db.models import Q
from django.contrib import auth


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    print(current_site)
    current_site = '127.0.0.1:8000'
    email_subject = 'Activate your account'
    email_body = render_to_string('activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    if not settings.TESTING:
        EmailThread(email).start()
        
def reset_password_email(user, request):
    current_site = get_current_site(request)
    print(current_site)
    current_site = '127.0.0.1:8000'
    email_subject = 'Reset your password'
    email_body = render_to_string('reset_password.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    if not settings.TESTING:
        EmailThread(email).start()


@auth_user_should_not_access
def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        username = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Password should be at least 6 characters')
            context['has_error'] = True

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Password mismatch')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Enter a valid email address')
            context['has_error'] = True

        if not username:
            messages.add_message(request, messages.ERROR,
                                 'Username is required')
            context['has_error'] = True

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,
                                 'Username is taken, choose another one')
            context['has_error'] = True

            return render(request, 'register.html', context, status=409)

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Email is taken, choose another one')
            context['has_error'] = True

            return render(request, 'register.html', context, status=409)

        if context['has_error']:
            return render(request, 'register.html', context)

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        if not context['has_error']:

            send_activation_email(user, request)

            messages.add_message(request, messages.SUCCESS,
                                 'We sent you an email to verify your account')
            return redirect('signin')

    return render(request, 'register.html')


@auth_user_should_not_access
def login_user(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        
        context = {'data': request.POST}
        if user and not user.is_email_verified:
            messages.add_message(request, messages.ERROR,
                                 'Email is not verified, please check your email inbox')
            return render(request, 'signin.html', context, status=401)
        else:
            print("email is verified")
        
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'signin.html')



def logout_user(request):

    logout(request)

    messages.add_message(request, messages.SUCCESS,
                         'Successfully logged out')

    return redirect(reverse('signin'))


def activate_user(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    print(user)
    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('signin'))

    return render(request, 'activate-failed.html', {"user": user})


def forget_password(request):
    if request.method == 'POST':
        # user = auth.authenticate()
        user = User.objects.filter(Q(username=request.POST.get('username')))
        if user:
            user = user[0]
            reset_password_email(user, request)
            messages.add_message(request, messages.SUCCESS,'We sent you an email to change your password')
        else:
            messages.add_message(request, messages.SUCCESS,
                             'User does not exist')
    return render(request, 'forget_password.html')

def reset_password(request, uidb64, token,user):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(password)

        if len(password) < 6:
            check =1
            messages.add_message(request, messages.ERROR,
                                 'Password should be at least 6 characters')
            context['has_error'] = True

        if password != password2:
            check =1
            messages.add_message(request, messages.ERROR,
                                 'Password mismatch')
            context['has_error'] = True
            
        if context['has_error']== False:
            user = User.objects.get(username=user)
            user.set_password(password)
            user.save()
            messages.add_message(request, messages.ERROR,
                                 'Updated Password')
            return redirect('signin')
            
    return render(request, 'update_password.html') 
    

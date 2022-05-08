from django.urls import path
from . import views


urlpatterns = [
    path('signin', views.login_user, name='signin'),
    path('register', views.register, name='signup'),
    path("logout_user", views.logout_user, name='logout'),
    path("forget_password", views.forget_password, name='forget_password'),
    path('activate-user/<uidb64>/<token>',views.activate_user, name='activate'),
    path('reset-password/<uidb64>/<token>/<str:user>',views.reset_password, name='reset'),
]

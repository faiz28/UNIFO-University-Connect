from django.urls import path,include
from . import views

urlpatterns = [
    path('register',views.register,name='signup'),
    path('login',views.login,name='signin'),
    path('logout',views.logout,name='logout'),
    path('user',views.user_profile,name='user'),
    path('user_update',views.user_update,name='user_update'),
    path('<int:dep_id>/department_registration',views.department_registration,name='department_registration'),
]
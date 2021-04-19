from django.urls import path,include
from . import views

urlpatterns = [
    path('publicuniversitylist/',views.publicuniversitylist,name='publicuniversitylist'),
    path('engineeruniversitylist/',views.engineeruniversitylist,name='engineeruniversitylist'),
    path('medicaluniversitylist/',views.medicaluniversitylist,name='medicaluniversitylist'),
    path('privateuniversitylist/',views.privateuniversitylist,name='privateuniversitylist'),
    path('agriculturaluniversitylist/',views.agriculturaluniversitylist,name='agriculturaluniversitylist'),
    path('stuuniversitylist/',views.stuuniversitylist,name='stuuniversitylist'),
    path('suuniversitylist/',views.suuniversitylist,name='suuniversitylist'),

    path('<int:uni_id>/uni_details/',views.uni_details,name='uni_details'),
    path('<int:dep_id>/department_deatils/',views.department_deatils,name='department_descrip'),
    path('<int:dep_id>/add_achievment/',views.add_achievment,name='add_achievment'),
    path('<int:acv_id>/achivment/',views.achiv_details,name='achiv_details'),
    path('<int:acv_id>/update_achievement/',views.update_achievement,name='update_achievement'),
]
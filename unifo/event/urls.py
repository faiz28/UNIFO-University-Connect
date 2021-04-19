from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:dep_id>/event_create',views.create,name='event_create'),
    path('<int:event_id>/event_details',views.event_view,name='event_view'),
    path('<int:dep_id>/event',views.uni_event,name='university_event'),
    path('<int:dep_id>/All_university_event',views.All_event,name='All_event'),
]
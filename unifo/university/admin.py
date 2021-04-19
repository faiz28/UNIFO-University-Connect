from django.contrib import admin
from .models import university_list,department_list,uni_cat,subject_list,university_name,achievment_list
# Register your models here.

admin.site.register(university_list)
admin.site.register(department_list)
admin.site.register(uni_cat)
admin.site.register(subject_list)
admin.site.register(university_name)
admin.site.register(achievment_list)

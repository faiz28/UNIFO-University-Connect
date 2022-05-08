from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class event_info(models.Model):
    username=models.CharField(max_length=100,default="u")
    uni_name=models.CharField(max_length=500,default="u")
    department_id=models.IntegerField(default=0)
    department_name=models.CharField(max_length=200,default="u")
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=500,default="")
    description = RichTextField(blank=True,null=True)
    date_start =  models.CharField(max_length=50,default="2011-08-19 02:40 PM")
    date_end = models.CharField(max_length=100,default="2011-09-19 02:40 PM")
    def __str__(self):
        return str(self.uni_name) 
    
from django.db import models
from account.models import userinfo
from ckeditor.fields import RichTextField
# Create your models here.


class uni_cat(models.Model):
    CHOICES = [
        ('ag', 'Agricultural'),
        ('en', 'Engineer'),
        ('pu', 'public'),
        ('pr', 'private'),
        ('me', 'medical'),
        ('st', 'Science and Technology universities'),
        ('su', 'Specialised universities'),

    ]
    uni_category = models.CharField(
        max_length=2,
        choices=CHOICES,
        default="",
    )
    def __str__(self):
        return self.uni_category

class subject_list(models.Model):
    sub_name = models.CharField(max_length=300,unique=True,default="")
    img = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.sub_name) 

class university_name(models.Model):
    university_name = models.CharField(max_length=300,unique=True,default="")
    
    def __str__(self):
        return self.university_name

class university_list(models.Model):
    uni_name=models.ForeignKey(university_name,on_delete=models.CASCADE,default="")
    uni_category=models.ForeignKey(uni_cat,on_delete=models.CASCADE,default="")
    university_logo = models.ImageField(upload_to='images/')
    established_year = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    application_link = models.URLField(max_length=200,default="")
    total_department=models.IntegerField(default=0)
    total_teacher=models.IntegerField(default=0)
    total_student=models.IntegerField(default=0)
    def __str__(self):
        return 'uni-cat: %s  ..............  uni_name: %s' %(self.uni_category.uni_category,self.uni_name.university_name)

class department_list(models.Model):
    uni_name = models.ForeignKey(university_name,on_delete=models.CASCADE)
    department_name=models.ForeignKey(subject_list,on_delete=models.CASCADE)
    established_year = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    # total_achievment=models.IntegerField(default=0)
    total_teacher=models.IntegerField(default=0)
    total_student=models.IntegerField(default=0)
    def __str__(self):
        return 'uni-name: %s  |||.....|||  depart_name: %s' %(self.uni_name,self.department_name.sub_name)


class achievment_list(models.Model):
    username=models.CharField(max_length=150,default="username")
    department_id=models.IntegerField(default=1)
    img = models.ImageField(upload_to='images/')
    title=models.CharField(max_length=1000)
    description = RichTextField(blank=True,null=True)

    def __str__(self):
        return 'username: %s  |||.....|||  title: %s' %(self.username,self.title)
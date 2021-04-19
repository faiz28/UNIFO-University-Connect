from django.db import models

# Create your models here.
class userinfo(models.Model):
    username=models.CharField(max_length=150,default="")
    fullname=models.CharField(max_length=150)
    address=models.CharField(max_length=1000)
    mobile_num=models.CharField(max_length=1000)
    profile_pic= models.ImageField(null=True,blank = True)
    work=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.username

class student_data(models.Model):
    username=models.CharField(max_length=150,default="")
    student_id=models.CharField(max_length=150)
    uni_name=models.CharField(max_length=150)
    department_name=models.CharField(max_length=150)
    department_id=models.IntegerField(default=0)
    # instagram=models.CharField(max_length=150)
    # facebook=models.CharField(max_length=150)

    def __str__(self):
        return self.student_id
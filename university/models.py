from django.db import models

# Create your models here.

class university(models.Model):
    Country=(
        ('F','Foreign'),
        ('B','Bangladesh'),
    )
    Bangladesh=(
        ('Pu','Public'),
        ('Pr','Private'),
        ('En','Engineering'),
        ('Me','Medical'),
    )

    img=models.ImageField(upload_to='uploads/% Y/% m/% d/')
    university_name=models.CharField(max_length=150)
    university_description=models.CharField(max_length=1000)
    link=models.URLField(max_length=128)
    country=models.CharField(max_length=1,choices=Country)
    catagory=models.CharField(max_length=3,choices=Bangladesh)

    def __str__(self):
        return self.university_name

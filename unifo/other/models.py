from django.db import models

# Create your models here.

class contact_form(models.Model):
    name=models.CharField(max_length=50)
    gmail=models.CharField(max_length=150)
    message=models.CharField(max_length=1500)

    def __str__(self):
        return self.gmail
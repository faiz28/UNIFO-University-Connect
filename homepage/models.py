from django.db import models

# Create your models here.

class category(models.Model):
    CHOICES = [
        ('pu', 'pulic'),
        ('pr', 'private'),
        ('me', 'medical'),
        ('en', 'Engineer'),
    ]
    university_category = models.CharField(
        max_length=2,
        choices=CHOICES,
        default="",
    )
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.university_category

from django.db import models
from django.contrib.auth.models import User


class Gender(models.Model):
    Gender_Options = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=Gender_Options)
    def __str__(self) -> str:
        return self.get_gender_display()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Using built-in user models to create a one to one relationship 

    profile_image = models.ImageField(upload_to='profile_image/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)
    short_bio = models.TextField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.user.username
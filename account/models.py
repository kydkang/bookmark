from django.db import models
from django.conf import settings

## To extend the User model -- based on Django 4 by Example -- Chapter 4 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)  ## optional field 
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)  #optional field

    def __str__(self):
        return f'Profile of {self.user.username}' 
    

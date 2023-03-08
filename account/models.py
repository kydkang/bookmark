from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

## To extend the User model -- based on Django 4 by Example -- Chapter 4 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)  ## optional field 
    photo = models.ImageField(_('photo'), upload_to='users/%Y/%m/%d', blank=True)  #optional field

    def __str__(self):
        return f'Profile of {self.user.username}' 
    

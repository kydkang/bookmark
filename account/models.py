from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)  ## optional field 
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)  #optional field

    def __str__(self):
        return f'Profile of {self.user.username}' 
    
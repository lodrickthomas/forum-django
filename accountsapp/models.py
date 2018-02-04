from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=200)


    # __str__(self):
    # self.UserProfile.name

    def __str__(self):
        return self.user.username



def create_user(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_user, sender=User)

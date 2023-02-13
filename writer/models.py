from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=100, blank = True, null = True,)
    username = models.CharField(max_length=100)
    email = models.EmailField(default='clinton@gmail.com')
    picture = models.ImageField(upload_to='img', default='img/user-default.png', blank = True, null = True,)
    profession = models.CharField(max_length = 500, blank = True, null = True,)
    bio = models.TextField()
    id = models. UUIDField(default = uuid.uuid4, editable = False, primary_key = True, unique = True)
    location = models.CharField(max_length = 200, blank = True, null = True,)
    # followers = models.ManyToManyField('Follower', related_name = 'followers')
    # followers_count = models.IntegerField(default=0)
    
    @property
    def pictureUrl(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.username

class Follower(models.Model):
    profile = models.OneToOneField(Profile, default = None, on_delete=models.CASCADE)


    def __str__(self):
        return self.profile.username



@receiver(post_save, sender=User)
def createProfile(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.email = instance.email
        profile.username = instance.username
        profile.save()

@receiver(post_delete, sender=Profile)
def deleteProfile(sender, instance, *args, **kwargs):
    profile = instance.user
    profile.delete()

@receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, *args, **kwargs):
    profile_user = instance.user
    if created == False:
        profile_user.name = instance.name
        profile_user.email = instance.email
        profile_user.username = instance.username
        profile_user.save()
        
        

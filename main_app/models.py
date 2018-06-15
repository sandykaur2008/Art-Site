from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 
# pylint: disable=E1101

# Create your models here.
class Piece(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  img_url = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField(max_length=200)

  def __str__(self):
    return self.body 

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(max_length=500, blank=True)
  img_url = models.CharField(max_length=100, blank=True)
  
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()
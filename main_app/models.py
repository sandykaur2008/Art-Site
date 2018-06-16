from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 
# pylint: disable=E1101

# Create your models here.
class Piece(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='piece_images',
                            default='media/default.png')

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
  image = models.ImageField(upload_to='profile_images',
                            default='media/default.png')
  
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()
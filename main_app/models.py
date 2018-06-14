from django.db import models

# Create your models here.
class Piece(models.Model):
  name = models.CharField()
  img_url = models.CharField()

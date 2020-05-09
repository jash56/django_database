from django.db import models

# Create your models here.

class  Hero(models.Model):
   
    name = models.CharField(max_length = 30)
    img = models.ImageField(upload_to='marvel')
    desc = models.TextField()
    weapon = models.CharField(max_length = 30)
    rank = models.IntegerField()

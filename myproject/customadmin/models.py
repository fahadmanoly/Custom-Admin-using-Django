from django.db import models

# Create your models here.

class AdminInfo(models.Model):
    email= models.CharField(max_length=20)
    username=models.CharField(max_length=30)
    password=models.TextField()

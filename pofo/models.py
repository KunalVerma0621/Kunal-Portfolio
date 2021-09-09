from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    phone=models.IntegerField()
    inbox=models.TextField(max_length=5000)
    time = models.DateTimeField(  auto_now_add=True,blank=True)

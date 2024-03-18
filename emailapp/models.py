from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Inbox(models.Model):
    username=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    subject=models.CharField(max_length=30)
    message=models.CharField(max_length=50)
    
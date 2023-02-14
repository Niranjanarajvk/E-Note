from django.db import models

# Create your models here.
class notedb(models.Model):
    NotesTitle=models.CharField(max_length=50,null=True,blank=True)
    NotesDescription=models.CharField(max_length=100,null=True,blank=True)

class regdb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    MobileNumber=models.IntegerField(null=True,blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)
    ConfirmPassword=models.CharField(max_length=50,null=True,blank=True)
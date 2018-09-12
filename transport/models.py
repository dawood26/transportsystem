from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Department (models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    def __str__(self):
        return '{} {}'.format(self.name,self.code)
#inheriting all properties of abstractUser from django package
class CustomUser(AbstractUser):
     #add additional fields in here
    phone = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=30, null=True)

    def __str__(self):
        return '{} {}'.format(self.username,self.email)

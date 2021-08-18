from django.db import models
from django.db.models.expressions import F

# Create your models here.

class signUp(models.Model):
    username = models.CharField('username', max_length=200, null=False, unique=True)
    password = models.CharField('password', max_length=200, null=False)
    confirm_password = models.CharField('confirm_password', max_length=200, null=False)

    def __str__(self):
        return self.username

class logIn(models.Model):
    username = models.CharField('username', max_length=200, null=False, unique=True)
    password = models.CharField('password', max_length=200, null=False)

    def __str__(self):
        return self.username
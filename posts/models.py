from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to= 'static/img')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=50)
    alt = models.CharField(max_length=50)
    image = models.ImageField(upload_to= 'static/img/portfolio')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
 
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password, liked_sport, created_date):



class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    liked_sport = models.JSONField(default=tuple, null=True)
    created_date = models.DateTimeField(auto_now_add=True)  

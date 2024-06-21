from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    liked_sport = models.JSONField(default=tuple)
    created_date = models.DateTimeField()

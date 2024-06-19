from django.db import models
from django.utils import timezone

from sport.models import Sport

# Create your models here.
def get_now_date():
    return timezone.now().date()

class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    liked_sport = models.ManyToManyField(Sport)
    created_date = models.DateTimeField(default=get_now_date)

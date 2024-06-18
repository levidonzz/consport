import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class User(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=40)
    gender = models.CharField(max_length=1, choices=GENDER)
    created_date = models.DateTimeField('created date')

    def __str__(self):
        return self.name


class Contest(models.Model):
    name = models.CharField(max_length=128)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    max_gamer_amount = models.IntegerField()
    current_gamer_amount = models.IntegerField()
    current_gamer = models.JSONField()
    game_date = models.DateTimeField('game date')
    description = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('published date')
    update_date = models.DateTimeField('update date')

    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

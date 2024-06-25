from django.contrib.auth.models import User
from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Contest(models.Model):
    name = models.CharField(max_length=128)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='contests')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_contest')
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_participants = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
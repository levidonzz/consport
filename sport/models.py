from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.dispatch import receiver
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model

from .utils import generate_avatar


User = get_user_model()

@receiver
def create_user_avatar(instance, created):
    if created:
        avatar_svg = generate_avatar(instance)
        avatar_filename = f'avatar_{instance.id}.svg'
        instance.avatar.save(avatar_filename, ContentFile(avatar_svg), save=True)


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
    participants = models.ManyToManyField(User, related_name='participated_contests', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class CustomUser(User):
    avatar = models.FileField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.username
    
    
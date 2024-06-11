from django.contrib import admin

from .models import User, Sport, Contest


# Register your models here.
admin.site.register((User, Sport, Contest))

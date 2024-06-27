from django.contrib import admin

from .models import Sport, Contest, CustomUser


# Register your models here.
admin.site.register(Sport)
admin.site.register(Contest)

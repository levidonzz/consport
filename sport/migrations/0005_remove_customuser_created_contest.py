# Generated by Django 4.2.13 on 2024-06-27 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0004_customuser_created_contest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='created_contest',
        ),
    ]
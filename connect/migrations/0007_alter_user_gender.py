# Generated by Django 4.2.13 on 2024-06-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0006_remove_user_liked_sport_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
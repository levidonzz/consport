# Generated by Django 4.2.13 on 2024-06-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0003_rename_max_pacticipants_contest_max_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contest',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

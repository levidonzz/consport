# Generated by Django 4.2.13 on 2024-06-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('created_date', models.DateTimeField()),
                ('liked_sport', models.ManyToManyField(to='sport.sport')),
            ],
        ),
    ]
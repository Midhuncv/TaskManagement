# Generated by Django 5.1.7 on 2025-03-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ConfirmPassword',
            field=models.CharField(default=False, max_length=150),
        ),
        migrations.AddField(
            model_name='user',
            name='Password',
            field=models.CharField(default=True, max_length=150),
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-30 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_remove_user_confirm_password_user_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='task',
            table='Task',
        ),
    ]

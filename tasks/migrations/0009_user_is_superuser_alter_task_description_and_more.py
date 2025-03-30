# Generated by Django 5.1.7 on 2025-03-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_task_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='', max_length=150),
        ),
    ]

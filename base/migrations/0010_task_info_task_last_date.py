# Generated by Django 4.0.3 on 2022-03-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_task_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='info',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Участники'),
        ),
        migrations.AddField(
            model_name='task',
            name='last_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
    ]

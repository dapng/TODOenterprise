# Generated by Django 4.0.3 on 2022-03-16 23:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_task_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='last_date',
            field=models.DateTimeField(default=datetime.date.today, null=True, verbose_name='Дата окончания'),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-06 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesTaches', '0004_alter_task_schedule_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 13, 16, 49, 56, 693433)),
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-26 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesTaches', '0009_alter_task_schedule_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 3, 17, 35, 48, 416953)),
        ),
    ]

# Generated by Django 3.2.25 on 2024-12-22 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0010_auto_20241222_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 12, 23, 17, 56, 24, 866892), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

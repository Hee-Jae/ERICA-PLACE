# Generated by Django 3.1.5 on 2021-01-16 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0003_auto_20210116_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
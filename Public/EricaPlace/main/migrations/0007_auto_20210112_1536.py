# Generated by Django 3.1.5 on 2021-01-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
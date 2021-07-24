# Generated by Django 3.1.6 on 2021-02-27 19:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rsv', '0006_reservation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='rsv_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_time',
            field=models.IntegerField(),
        ),
    ]
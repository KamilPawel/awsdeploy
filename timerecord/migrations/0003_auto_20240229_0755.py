# Generated by Django 3.1.14 on 2024-02-29 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timerecord', '0002_time_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

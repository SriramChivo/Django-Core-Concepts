# Generated by Django 2.1.5 on 2020-05-24 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0015_auto_20200524_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummy',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 2.1.5 on 2020-05-24 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0009_auto_20200524_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummy',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

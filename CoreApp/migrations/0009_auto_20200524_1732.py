# Generated by Django 2.1.5 on 2020-05-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0008_dummy_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummy',
            name='Date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

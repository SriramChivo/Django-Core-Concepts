# Generated by Django 2.1.5 on 2020-05-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0019_auto_20200524_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummy',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

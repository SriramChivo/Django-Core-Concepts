# Generated by Django 2.1.5 on 2020-05-26 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classBasedCoreApp', '0003_auto_20200526_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='remarks',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]

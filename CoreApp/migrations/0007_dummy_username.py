# Generated by Django 2.1.5 on 2020-05-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0006_auto_20200524_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummy',
            name='UserName',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]

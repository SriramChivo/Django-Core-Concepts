# Generated by Django 2.1.5 on 2020-05-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0010_auto_20200524_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummy',
            name='files',
            field=models.FileField(default='', upload_to=None),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.1.5 on 2020-05-25 06:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0021_auto_20200525_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummy',
            name='UpdatedDate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dummy',
            name='publishedDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

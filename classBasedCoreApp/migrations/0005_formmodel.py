# Generated by Django 2.1.5 on 2020-05-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classBasedCoreApp', '0004_login_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=65)),
                ('lastanme', models.CharField(max_length=65)),
                ('Age', models.IntegerField()),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('publishedTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

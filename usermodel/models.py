from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AdditionalUserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Hobby = models.CharField(max_length=50, blank=True)
    Favourite_Sport = models.CharField(max_length=100, blank=True)
    Working_Place = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Experience = models.IntegerField()


class Blog(models.Model):
    Blog = models.ForeignKey(User, related_name='blog',
                             on_delete=models.CASCADE)
    Item = models.CharField(max_length=120)
    description = models.CharField(max_length=120)

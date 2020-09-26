from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


# Create your models here.


def customvalidate(value):
    if(value == 'raj'):
        raise ValidationError('Please add someother description')


class login(models.Model):
    username = models.CharField(max_length=65, unique=True)
    description = models.TextField(max_length=50,
                                   validators=[customvalidate])
    about = models.CharField(max_length=35, blank=True)
    remarks = models.CharField(max_length=35, blank=True)
    updateTime = models.DateTimeField(auto_now=True)
    publishedTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("detailView", kwargs={"pk": self.pk})

    # def get_absolute_url(self)


# def validate_firstname(value):
#     print('--------------------')
#     print('From models')
#     value = 'constant no change'  # whatever we set it wont reflect in django model
#     print(value)
#     raise ValidationError('whatever you enter i shos error')


class FormModel(models.Model):
    firstname = models.CharField(
        max_length=65)  # , validators=[validate_firstname] if validator enabled above function
    lastname = models.CharField(max_length=65)
    Age = models.IntegerField()
    updateTime = models.DateTimeField(auto_now=True)
    publishedTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.firstname) + ' '+str(self.lastname)

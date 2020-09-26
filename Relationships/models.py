from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class City(models.Model):
    Name = models.CharField(max_length=120)
    Zipcode = models.CharField(max_length=6, validators=[
                               RegexValidator(r'^\d{1,10}$', message='Only Numericals is allowed')])

    def __str__(self):
        return self.Name


class Address(models.Model):
    Housenum = models.IntegerField()
    Housename = models.CharField(max_length=120)
    Streetname = models.CharField(max_length=120)
    City = models.ForeignKey(City, on_delete=models.CASCADE)


def __str__(self):
    return self.Streetname


class Toppings(models.Model):
    Topname = models.CharField(max_length=120)

    def __str__(self):
        return self.Topname


class Pizza(models.Model):
    PizzaName = models.CharField(max_length=120)
    toppings = models.ManyToManyField('Toppings')

    def __str__(self):
        return self.PizzaName

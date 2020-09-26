from django.db import models

# Create your models here.


class City(models.Model):
    cityName = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural="City"

    def __str__(self):
        return self.cityName


class Customer(models.Model):
    Name = models.CharField(max_length=120)
    Address = models.CharField(max_length=120)
    City = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Customer"

    def __str__(self):
        return self.Name


class Tags(models.Model):
    ProductTags = models.CharField(max_length=120, null=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.ProductTags


class Products(models.Model):
    ProdName = models.CharField(max_length=120)
    tags = models.ManyToManyField(Tags)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.ProdName


class Orders(models.Model):
    quantity = models.IntegerField(default=1)
    Price = models.IntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.customer.Name

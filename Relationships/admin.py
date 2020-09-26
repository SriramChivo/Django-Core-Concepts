from django.contrib import admin
from .models import Address, City, Pizza, Toppings
# Register your models here.
admin.site.register(Address)
admin.site.register(City)
admin.site.register(Pizza)
admin.site.register(Toppings)

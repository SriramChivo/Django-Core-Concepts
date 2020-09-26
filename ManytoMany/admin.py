from django.contrib import admin
from .models import Tags, Orders, Products, Customer, City


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Address', 'Dummy']
    search_fields = ['Name', 'Address', 'City']
    raw_id_fields = ['City']

    def Dummy(self, obj):
        print(obj._meta.get_fields())
        print(obj)
        print('----------------')
        print(self.list_display)
        return obj.Name


class CityAdmin(admin.ModelAdmin):
    search_fields = ['cityName']


# Register your models here.
admin.site.register(City, CityAdmin)
admin.site.register(Tags)
admin.site.register(Orders)
admin.site.register(Products)
admin.site.register(Customer, CustomerAdmin)

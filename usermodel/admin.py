from django.contrib import admin
from .models import AdditionalUserInfo,Blog
# Register your models here.


class Addadmin(admin.ModelAdmin):
    class Meta:
        model = AdditionalUserInfo
        list_display = ['Working_Place', 'Company', 'Experience']
        search_fields = ['Working_Place', 'Company', 'Experience']


admin.site.register(AdditionalUserInfo, Addadmin)
admin.site.register(Blog)
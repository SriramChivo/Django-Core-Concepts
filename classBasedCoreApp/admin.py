from django.contrib import admin
from .models import login, FormModel
# Register your models here.


class loginadmin(admin.ModelAdmin):
    fields = (
        'username',
        'description'
        'about',
        'updateTime',
        'publishedTime',
    )
    readonly_fields = ('updateTime', 'publishedTime')


class formadmin(admin.ModelAdmin):
    fields = (
        'firstname',
        'lastname',
        'Age',
    )
    readonly_fields = ('updateTime', 'publishedTime')


admin.site.register(login, loginadmin)
admin.site.register(FormModel, formadmin)

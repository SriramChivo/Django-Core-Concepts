from django.contrib import admin
from .models import Person, Dummy
# Register your models here.

admin.site.register(Person)


class DummyAdmin(admin.ModelAdmin):
    fields = (
        'UserName',
        'number',
        'slug',
        'Date',
        'options',
        'files',
        'getage',
        'UpdatedDate',
        'publishedDate',
    )
    readonly_fields = (
        'UpdatedDate',
        'publishedDate',
        'getage',
    )

    def getage(self, obj, *args, **kwargs):
        # if Property decorator is not included then return (obj.property())
        return obj.property

    class Meta:
        model = Dummy


admin.site.register(Dummy, DummyAdmin)

from django.contrib import admin
from .models import View,  Product2, Yrok2

admin.site.register(Product2)
admin.site.register(View)


@admin.register(Yrok2)
class Yrok2Admin(admin.ModelAdmin):
    list_display = ['name', 'view', 'view_status']
    list_editable = ['view']

    @admin.display(ordering='view', description='Статус')
    def view_status(self, yrok: Yrok2):
        if yrok.view >= 200:
              return 'Просмотрено'
        else:
            return 'Не просмотрено'

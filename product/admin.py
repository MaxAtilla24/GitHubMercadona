from django.contrib import admin
from . import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productName',)

admin.site.register(models.Product, ProductAdmin)

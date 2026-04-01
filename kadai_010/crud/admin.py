from django.contrib import admin
from .models import Product
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=("types", "title" )
    list_filter=("types",)

admin.site.register(Product, ProductAdmin)

from django.contrib import admin
from .models import Product, ProductCategory, SubCategory, Color


class ProductAdmin(admin.ModelAdmin):
    # Let you to search with first name, last name and phone number of the customer
    search_fields = ['sku','title', 'description']
    list_filter = ['category']
    list_display =['title', 'category', 'sku']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display =['name', 'category']
   

# Register your models here.

admin.site.register(Product, ProductAdmin )
admin.site.register(ProductCategory)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Color)


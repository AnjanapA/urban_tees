from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):

    list_display =(
    'item_image',
    'item_name',
    'item_description',
    'new_price',
    'old_price',
    'offer',
    'category'
    )
admin.site.register(Product,ProductAdmin)

from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):

    list_display =(
    'item_image1',
    'item_image2',
    'item_image3',
    'item_image4',
    'item_name',
    'item_description',
    'new_price',
    'old_price',
    'offer',
    'category',
    'small_size',
    'medium_size',
    'large_size',
    'extralarge_size',


    )
admin.site.register(Product,ProductAdmin)
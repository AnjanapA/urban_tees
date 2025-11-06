from django.contrib import admin
from .models import Product,User,Cart

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
    # 'wishlist'


    )
admin.site.register(Product,ProductAdmin)

class UserAdmin(admin.ModelAdmin):

    list_display =(
    'username',
    'email',
    'phone',
    'gender',
    'address',
    'place',
    'city',
    'pincode',
    'role',
    'activity',
    'password',
    )
admin.site.register(User,UserAdmin)


class CartAdmin(admin.ModelAdmin):

    list_display =(
    'user_id',
    'product_id',
    'product_name',
    'product_price',
    'quantity',
    'size',
    'oreder_item',
    'product_image',
    'user_content',
    'user_image',
    'user_text',
    )
admin.site.register(Cart,CartAdmin)
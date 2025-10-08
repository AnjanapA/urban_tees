from django.contrib import admin
from .models import Product,User

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
    'address',
    'place',
    'city',
    'pincode',
    'role',
    'activity',
    'password',
    'confirm_password'
    )
admin.site.register(User,UserAdmin)
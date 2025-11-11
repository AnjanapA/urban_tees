from django.contrib import admin
from .models import Product,User,Order

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


class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'order_code',
        'user',
        'product',
        'quantity',
        'size',
        'payment_method',
        'payment_status',
        'order_status',
        'total_amount',
        'total_discount',
    )
admin.site.register(Order,OrderAdmin)
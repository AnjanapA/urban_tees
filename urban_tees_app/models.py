from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('mens', 'Mens'),
        ('womens', 'Womens'),
        ('girls', 'Girls'),
        ('boys', 'Boys'),
    ]
    item_image1 = models.CharField(max_length=255)
    item_image2 = models.CharField(max_length=255)
    item_image3 = models.CharField(max_length=255)
    item_image4 = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    new_price = models.IntegerField()
    old_price = models.IntegerField()
    offer = models.IntegerField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    small_size=models.IntegerField()
    medium_size=models.IntegerField()
    large_size=models.IntegerField()
    extralarge_size=models.IntegerField()
    # wishlist=models.BooleanField()


    def __str__(self):
        return self.item_name


# class Login(models.Model):
#     user_name=models.CharField(max_length=255)
#     password=models.CharField(max_length=8)

# class Register(models.Model):
#     full_name=models.CharField(max_length=255)
#     mail=models.EmailField(_(""), max_length=254)
#     address=models.CharField(max_length=255)
#     models.PhoneNumberField(_(""))
#     models.EmailField(_(""), max_length=254)

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # def create_superuser(self,email,password=None,**extra_fields):
    #     extra_fields.setdefault('is_superuser',True)
    #     return set.create_user(email,password,**extra_fields)


class User(AbstractUser):
    ROLES = [
    ('user', 'User'),
    ('admin', 'Admin'),
        ]
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ]
    user_name = models.CharField(max_length=150, unique=True)
    email=models.EmailField("Email", max_length=254,unique=True)
    phone=models.CharField("Phone", max_length=255)
    gender=models.CharField(max_length=10, choices=GENDER)
    address=models.CharField(max_length=255)
    place=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    pincode=models.CharField(max_length=6)
    role=models.CharField(max_length=10, choices=ROLES)
    activity=models.CharField(max_length=255)
    password=models.CharField(max_length=8)
    # username = models.CharField(max_length=150, unique=True,null=True)
    objects=CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS=['user_name','password']

    
    def __str__(self):
        return self.email

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.product.item_name}"



class Order(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='orders'  # all orders belonging to this user
    )

    product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        related_name='orders',  # all orders that include this product
        null=True
    )

    SIZE = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('extralarge', 'Extra Large'),
    ]
    size = models.CharField(max_length=10, choices=SIZE)
    quantity = models.IntegerField()

    user_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    user_text = models.CharField(max_length=255, null=True, blank=True)

    net_amount = models.IntegerField(null=True)
    total_amount = models.IntegerField(null=True)
    total_discount = models.IntegerField(null=True)

    order_code = models.CharField(max_length=50)

    PAYMENT_METHOD_CHOICES = [
        ('cash_on_delivery', 'Cash on Delivery'),
        ('online_payment', 'Online Payment'),
        ('card_payment', 'Card Payment'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)

    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    order_status = models.CharField(max_length=15, choices=ORDER_STATUS_CHOICES)

    def __str__(self):
        product_name = self.product.name if self.product else "No Product"
        return f"Order {self.order_code} - {product_name}"

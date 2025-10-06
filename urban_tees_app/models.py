from django.db import models
import json

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


class User(models.Model):
    username=models.CharField(max_length=255)
    mail=models.EmailField("Email", max_length=254)
    phone=models.CharField("Phone", max_length=255)
    address=models.CharField(max_length=255)
    place=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    pincode=models.CharField(max_length=6)
    role=models.CharField(max_length=255)
    activity=models.CharField(max_length=255)
    password=models.CharField(max_length=8)


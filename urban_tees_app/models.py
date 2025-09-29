from django.db import models

# Create your models here.



class Product(models.Model):
    item_image = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    new_price = models.IntegerField()
    old_price = models.IntegerField()
    offer = models.IntegerField()
    category = models.CharField(max_length=255)
    item_quantity=models.IntegerField()
    item_size=models.CharField(max_length=255)


 




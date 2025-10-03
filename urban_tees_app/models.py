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
    # category = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    # item_quantity = models.IntegerField()
    small_size=models.IntegerField()
    medium_size=models.IntegerField()
    large_size=models.IntegerField()
    extralarge_size=models.IntegerField()

    # item_size = models.TextField(default='[]', blank=True)

    # def set_sizes(self, sizes_list):
    #     self.item_sizes = json.dumps(sizes_list)

    # def get_sizes(self):
    #     return json.loads(self.item_sizes)

    def __str__(self):
        return self.item_name

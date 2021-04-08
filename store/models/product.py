from django.db.models.deletion import CASCADE
from django.db import models
from .category import Category
from .brand import Brand


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    previous_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    specification = models.CharField(max_length=300, default='', null=True, blank=True)
    rating = models.IntegerField(default=5)

    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_product_orderby_10():
        return Product.objects.order_by('id')[:9]

    @staticmethod
    def get_all_product():
        return Product.objects.all()
    
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)

    
    @staticmethod
    def get_all_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_product()
    
    @staticmethod
    def get_product_by_id_for_image(producty_id):
        return Product.objects.filter(id = producty_id)
    
    @staticmethod
    def get_product_price():
        return Product.objects.values_list('price')
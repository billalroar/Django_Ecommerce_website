from django.db.models.deletion import CASCADE
from django.db import models
from .category import Category
from .brand import Brand
from .product import Product
from .user import User
import datetime

class Orders(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='',blank=True)
    total = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    payment = models.CharField(max_length=50,default='',blank=True)
    date = models.DateField(default= datetime.datetime.today)
    status = models.BooleanField(default= False)
    first_name = models.CharField(max_length=50,default='',blank=True)
    last_name = models.CharField(max_length=50,default='',blank=True)
    email = models.CharField(max_length=50,default='',blank=True)
    country = models.CharField(max_length=50,default='',blank=True)
    city = models.CharField(max_length=50,default='',blank=True)
    state = models.CharField(max_length=50,default='',blank=True)
    zip_code = models.CharField(max_length=50,default='',blank=True)


    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders\
            .objects\
            .filter(customer = customer_id)\
            .Order_by('-date')
    
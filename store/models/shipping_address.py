from django.db.models.deletion import CASCADE
from django.db import models
from .user import User


class Shipping_address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50,default='',blank=True)
    country = models.CharField(max_length=50,default='',blank=True)
    city = models.CharField(max_length=50,default='',blank=True)
    state = models.CharField(max_length=50,default='',blank=True)
    zip_code = models.CharField(max_length=50,default='',blank=True)
    
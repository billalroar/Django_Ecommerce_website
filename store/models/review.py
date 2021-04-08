from django.db.models.deletion import CASCADE
from django.db import models
import datetime

class Review(models.Model):
    product_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=500, default='', null=True, blank=True)
    date = models.DateField(default= datetime.datetime.today)
    rating = models.IntegerField(default=5)

    def register(self):
        self.save()

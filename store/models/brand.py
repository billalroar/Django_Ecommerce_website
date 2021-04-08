from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/brands/')

    def __str__(self):
        return self.name


    @staticmethod
    def get_all_brand():
        return Brand.objects.all()
from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.brand import Brand
from .models.user import User
from .models.contact import Contact
from .models.review import Review
from .models.orders import Orders
from .models.shipping_address import Shipping_address


# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name', 'price' ,'category', 'brand','rating','previous_price']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminBrand(admin.ModelAdmin):
    list_display = ['name']


class AdminUser(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email','password']

class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

class AdminReview(admin.ModelAdmin):
    list_display = ['name','email','message','rating']

class AdminOrders(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price','status','date','payment']

class AdminShipping_address(admin.ModelAdmin):
    list_display = ['user_id','address','city','state','zip_code','country']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Brand, AdminBrand)
admin.site.register(User, AdminUser)
admin.site.register(Contact, AdminContact)
admin.site.register(Review, AdminReview)
admin.site.register(Orders, AdminOrders)
admin.site.register(Shipping_address, AdminShipping_address)

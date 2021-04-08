from django import template
from store.models.brand import Brand
from store.models.review import Review

register = template.Library()


@register.filter(name='cart_quantity')
def cart_quantity(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;

@register.filter(name='price_total')
def price_total(product , cart):
    return product.price * cart_quantity(product,cart)
    
@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0;
    for p in products:
        sum += int(price_total(p,cart))
    return sum

@register.filter(name='currency')
def currency(number):
    return 'TK '+str(number)

@register.filter(name='full_total')
def full_total(products, cart):
    sum = 0;
    for p in products:
        sum += int(price_total(p,cart))
    return 60 + sum

@register.filter(name='brand')
def brand():
    brand = Brand.get_all_brand();
    return brand

@register.filter(name='rating')
def rating(num):
    return range(num)

@register.filter(name='specification')
def specification(text): 
    t=text.split(",")
    se=[]
    for s in t:
        se.append(" "+s.strip())
    return se

@register.filter(name='review')
def review(id):
    t= Review.objects.filter(product_id=id)[:5]
    return t

@register.filter(name='single_full_total')
def single_full_total(price,quantity):
    t= (price*int(quantity))+60
    return t



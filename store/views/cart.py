from django.views import View
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.brand import Brand
from store.models.product import Product
from store.models.user import User
from store.models.category import Category



class Cart(View):

    def get(self, request):
        cart = request.session.get('cart')
        dic ={}
        if cart:
            ids = cart.keys()
            products = Product.get_product_by_id(ids)
            dic['products'] = products

        return render(request, 'cart.html',dic)


    def post(self, request):
        action = request.POST.get('action')
        if action == 'plus':
            product_id = request.POST.get('product_id')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product_id)
                if quantity:
                    if quantity>=1:
                        cart[product_id] = quantity+1
                    else:
                        cart[product_id] = quantity
            request.session['cart'] = cart
            return redirect('cartpage')
        if action == 'minus':
            product_id = request.POST.get('product_id')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product_id)
                if quantity:
                    if quantity<=1:
                        cart[product_id] = quantity
                    else:
                        cart[product_id] = quantity-1
            request.session['cart'] = cart
            return redirect('cartpage')
        if action == 'remove':
            product_id = request.POST.get('product_id')
            cart = request.session.get('cart')
            if cart:
                if product_id:
                    cart.pop(product_id)
            request.session['cart'] = cart
            return redirect('cartpage')
        
        return redirect('cartpage')
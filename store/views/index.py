from django.views import View
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.brand import Brand
from store.models.product import Product
from store.models.user import User



class Index(View):

    def get(self, request):
        dic ={}
        brands = Brand.get_all_brand();
        first_10_product = Product.get_all_product()
        
        
        cart_product = request.GET.get('cart')
        wishlist_product = request.GET.get('wishlist')
        if cart_product:
            session_cart = request.session.get('cart')
            if session_cart:
                quantity = session_cart.get(cart_product)
                if quantity:
                    session_cart[cart_product] = quantity+1
                else:
                    session_cart[cart_product] = 1
            else:
                session_cart = {}
                session_cart[cart_product] = 1
            request.session['cart'] = session_cart
            print('cart  ',request.session['cart'])
        elif wishlist_product:
            session_wishlist = request.session.get('wishlist')
            if session_wishlist:
                quantity = session_wishlist.get(wishlist_product)
                if quantity:
                    session_wishlist[wishlist_product] = quantity+1
                else:
                    session_wishlist[wishlist_product] = 1
            else:
                session_wishlist = {}
                session_wishlist[wishlist_product] = 1
            request.session['wishlist'] = session_wishlist
            print('wishlist  ',request.session['wishlist'])
        


        dic['brands'] = brands
        dic['first_10_product'] = first_10_product
        return render(request, 'index.html', dic)
from django.views import View
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.brand import Brand
from store.models.product import Product
from store.models.user import User
from store.models.category import Category



class Wishlist(View):

    def get(self, request):
        wishlist = request.session.get('wishlist')
        dic ={}
        if wishlist:
            ids = wishlist.keys()
            products = Product.get_product_by_id(ids)
            dic['products'] = products

        return render(request, 'wishlist.html',dic)


    def post(self, request):
        action = request.POST.get('action')
        if action == 'plus':
            product_id = request.POST.get('product_id')
            wishlist = request.session.get('wishlist')
            if wishlist:
                quantity = wishlist.get(product_id)
                if quantity:
                    if quantity>=1:
                        wishlist[product_id] = quantity+1
                    else:
                        wishlist[product_id] = quantity
            request.session['wishlist'] = wishlist
            return redirect('wishlistpage')
        if action == 'minus':
            product_id = request.POST.get('product_id')
            wishlist = request.session.get('wishlist')
            if wishlist:
                quantity = wishlist.get(product_id)
                if quantity:
                    if quantity<=1:
                        wishlist[product_id] = quantity
                    else:
                        wishlist[product_id] = quantity-1
            request.session['wishlist'] = wishlist
            return redirect('wishlistpage')
        if action == 'remove':
            product_id = request.POST.get('product_id')
            wishlist = request.session.get('wishlist')
            if wishlist:
                if product_id:
                    wishlist.pop(product_id)
            request.session['wishlist'] = wishlist
            return redirect('wishlistpage')

        if action == 'add_cart':
            product_id = request.POST.get('product_id')
            wishlist = request.session.get('wishlist')
            cart = request.session.get('cart')
            if wishlist:
                if product_id:
                    quantity = wishlist.get(product_id)
                    if cart:
                        keys = cart.keys()
                        is_it=None
                        for id in keys:
                            if int(id) == int(product_id):
                                is_it = "True"
                            else:
                                pass
                        if is_it:
                            quantity2 = cart.get(product_id)
                            cart[product_id] = int(quantity)+int(quantity2)
                            wishlist.pop(product_id)   
                            request.session['wishlist'] = wishlist   
                            request.session['cart'] = cart
                        else:
                            cart[product_id] = quantity
                            wishlist.pop(product_id)  
                            request.session['wishlist'] = wishlist 
                            request.session['cart'] = cart  
                    else:
                        cart = {}
                        cart[product_id] = quantity
                        request.session['cart'] = cart
                        request.session['wishlist'] = wishlist
            return redirect('wishlistpage')
        
        return redirect('wishlistpage')
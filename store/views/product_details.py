from store.views.cart import Cart
from django.views import View
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render,redirect
from store.models.brand import Brand
from store.models.product import Product
from store.models.user import User
from store.models.category import Category
from store.models.review import Review
import re
from django.http.response import JsonResponse

class Product_detail(View):

    def get(self, request):
        dic ={}
        product_view_id = request.GET.get('search')
        product_quantity= request.GET.get('action')
        quantity=request.GET.get('quantity')
        dic['search_id'] = product_view_id
        print(product_view_id)
        if not quantity:
            quantity = 1
            print(quantity)
        else:
            if product_quantity:
                if product_quantity == 'plus':
                    if int(quantity)>0:
                        print(quantity)
                        quantity=int(quantity)+1
                elif product_quantity == 'minus':
                    if int(quantity)>1:
                        print(quantity)
                        quantity=int(quantity)-1
        dic['quantity'] = int(quantity)


        cart_product = request.GET.get('cart')
        wishlist_product = request.GET.get('wishlist')
        cart1=request.GET.get('cart1')
        if cart_product:
            session_cart = request.session.get('cart')
            if session_cart:
                quantity1 = session_cart.get(cart_product)
                if quantity1:
                    session_cart[cart_product] = quantity1+1
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
                quantity2 = session_wishlist.get(wishlist_product)
                if quantity2:
                    session_wishlist[wishlist_product] = quantity2+1
                else:
                    session_wishlist[wishlist_product] = 1
            else:
                session_wishlist = {}
                session_wishlist[wishlist_product] = 1
            request.session['wishlist'] = session_wishlist
            print('wishlist  ',request.session['wishlist'])
        elif cart1:
            session_cart = request.session.get('cart')
            if session_cart:
                quantity3 = session_cart.get(cart1)
                if quantity3:
                    if quantity:
                        session_cart[cart1] = quantity3+int(quantity)
                    else:
                        session_cart[cart1] = quantity3+1
                else:
                    if quantity:
                        session_cart[cart1] = int(quantity)
                    else:
                        session_cart[cart1] = 1        
            else:
                if quantity:
                    session_cart = {}
                    session_cart[cart1] = int(quantity)
                    print(session_cart[cart1])
                else:
                    session_cart = {}
                    session_cart[cart1] = 1
            request.session['cart'] = session_cart
            print('cart  ',request.session['cart'])



        if product_view_id:
            dic['view_product'] = Product.objects.filter(id=product_view_id)
        brands = Brand.get_all_brand();
        product_all = Product.objects.all();
        b={}
        if brands:
            for n in brands:
                b[str(n)]=str(len(Product.objects.filter(brand = n)))
            dic['br']=b 
        dic['brands'] = brands
        dic['first_10_product'] = product_all
        # for i in brands:
        #     print(i.image)
        return render(request, 'product-detail.html' , dic)
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        review = request.POST.get('review')
        product_id = request.POST.get('product_id')
        rating = request.POST.get('review_value')
        error_massage = None
        print(name,email,review,product_id,rating)
        if not name:
            error_massage = "Name Required !!"
        elif not email:
            error_massage = "Email Required !!"
        elif re.match("^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", email) == None:
            error_massage = "Email Not Valid !!"
        elif not review:
            error_massage = "Write Review !!"
        elif not rating:
            error_massage = "Give Rating !!"
            
            
        if error_massage:
            return JsonResponse({'error_massage': error_massage,
                                     'url':'/product-detail?search='+product_id,
                                     'success': False})
        else:
            obj = Review(product_id=product_id,name=name,message=review,email=email,rating=rating)
            obj.register()
            p_rating = Product.objects.get(id=product_id)
            n_rating =int((int(p_rating.rating) + int(rating)) / 2)
            update_product = Product.objects.filter(id = product_id).update(rating = n_rating)
            return JsonResponse({'error_massage': error_massage,
                                     'url':'/product-detail?search='+product_id,
                                     'success': True})
        
        # dic ={}
        # dic['view_product'] = Product.objects.filter(id=product_id)
        # brands = Brand.get_all_brand();
        # product_all = Product.objects.all();
        # dic['brands'] = brands
        # dic['first_10_product'] = product_all
        # for i in brands:
        #     print(i.image)
        # return render(request, 'product-detail.html' , dic)
    
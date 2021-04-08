from django.http.response import JsonResponse
from store.views.cart import Cart
from django.views import View
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render,redirect
from store.models.brand import Brand
from store.models.product import Product
from store.models.user import User
from store.models.category import Category
from store.models.orders import Orders
from store.models.shipping_address import Shipping_address



class Checkout(View):

    

    def get(self, request):
        dic ={}
        product_from= request.GET.get('buy')
        quantity= request.GET.get('quantity')
        if product_from == 'cart':
            cart = request.session.get('cart')
            if cart:
                ids = cart.keys()
                products = Product.get_product_by_id(ids)
                dic['products'] = products
                dic['for'] = "cart"
        elif product_from == 'single':
            product_id= request.GET.get('product_id')
            if product_id:
                ids = product_id
                products = Product.objects.filter(id=ids)
                print(list(products))
                dic['product'] = products
                dic['for'] = product_id
                if not quantity:
                    dic['quantity'] = 1
                else:
                    dic['quantity'] = quantity
        
        customer_id = request.session.get("customer_id")
        
        dic['user_details'] = Shipping_address.objects.filter(id = customer_id)
        # cart = request.session.get('cart')
        # if cart:
        #         ids = "7"
        #         products = Product.objects.filter(id=ids)
        #         print(products)
        #         dic['product'] = products
        return render(request, 'checkout.html', dic)

    def post(self, request):
        
        customer = request.session.get('customer_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        total = request.POST.get('total')
        phone = request.POST.get('phone')
        payment = request.POST.get('payment')
        email = request.POST.get('email')
        country = request.POST.get('country')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        for_do=request.POST.get('for')
        error_massage = None
        print(customer,address,total,phone,payment,first_name,last_name,email,country,city,state,zip_code,for_do)
        
        if not first_name:
            error_massage = "First Name Required !!"
        elif not address:
            error_massage = "address Required !!"
        elif not total:
            error_massage = "something wrong !!"
        elif not phone:
            error_massage = "Mobile Number Required !!"
        elif len(phone) <11:
            error_massage = "Mobile Number Not Valid !!"
        elif not payment:
            error_massage = "select payment method !!"
        elif not email:
            error_massage = "Email Required !!"
        elif not country:
            error_massage = "Select Country !!"
        elif not city:
            error_massage = "City Required !!"
        elif not state:
            error_massage = "State Required !!"
        elif not zip_code:
            error_massage = "Zipe Code Required !!"
        
        if for_do =='cart':
            cart = request.session.get('cart')
            if not cart:
                error_massage = "No cart Product !!" 
            if error_massage:
                return JsonResponse({'error_massage': error_massage,
                                     'url':'/product-list',
                                     'success': False})
            else:
                products = Product.get_product_by_id(list(cart.keys()))
                for product in products:
                    order = Orders(customer = User(id=customer),
                            product = product,
                            quantity=cart.get(str(product.id)),
                            price = product.price,
                            address=address,
                            total = str(int(product.price)*int(cart.get(str(product.id)))),
                            phone = phone,
                            payment = payment,
                            first_name = first_name,
                            last_name = last_name,
                            email = email,
                            country = country,
                            city = city,
                            state = state,
                            zip_code = zip_code,
                            )
                    order.placeOrder() 
                request.session['cart']={}
                return JsonResponse({'error_massage': error_massage,
                                     'url':'/product-list',
                                     'success': True})
        else:
            if not for_do:
                error_massage = "No Product Found !!"
            if error_massage:
                return JsonResponse({'error_massage': error_massage,
                                     'url':'/product-list',
                                     'success': False})
            else:
                quantity = request.POST.get('quantity')
                if not quantity:
                    quantity='1'
                products = Product.objects.filter(id=int(for_do))
                for product in products:
                    order = Orders(customer = User(id=customer),
                            product = product,
                            quantity=str(quantity),
                            price = product.price,
                            address=address,
                            total = str(int(product.price)*int(str(quantity))),
                            phone = phone,
                            payment = payment,
                            first_name = first_name,
                            last_name = last_name,
                            email = email,
                            country = country,
                            city = city,
                            state = state,
                            zip_code = zip_code,
                            )
                order.placeOrder()
                return JsonResponse({'error_massage': error_massage,
                                     'url':'/product-list',
                                     'success': True})
                
        
        

        

        

from django.http.response import JsonResponse
from store.models import shipping_address
from store.views.cart import Cart
from django.views import View
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render,redirect
from store.models.brand import Brand
from store.models.product import Product
from store.models.user import User
from store.models.shipping_address import Shipping_address
from store.models.orders import Orders
import re
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password,check_password


class Myaccount(View):

    def get(self, request):
        dic ={}
        customer_id =request.session.get('customer_id')
        orders_all = Orders.objects.filter(customer = customer_id)
        dic['orders'] = orders_all
        get_address = Shipping_address.objects.filter(user_id = customer_id)
        dic['get_address'] = get_address
        user = User.objects.filter(id = customer_id)
        dic['users'] = user

        return render(request, 'my-account.html', dic)
    
    def post(self, request):
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        state = request.POST.get('state')
        value = request.POST.get('value')
        customer_id =request.session.get('customer_id')
        error_massage = None

        if value == 'update_address':
            if not address:
                error_massage = "Address Required !!"
            elif not city:
                error_massage = "City Required !!"
            elif not zip_code:
                error_massage = "Zip Code Required !!"
            elif not country:
                error_massage = "Country Required !!"
            elif not state:
                error_massage = "state Required !!"
            if error_massage:
                return JsonResponse({'error_massage': error_massage,
                                     'url':'/my-account',
                                     'success': False})
            else:
                get_address = Shipping_address.objects.filter(user_id = customer_id).values()
                if get_address:
                    update_address = Shipping_address.objects.filter(user_id = customer_id).update(user_id = User(id=customer_id)
                    ,address=address,country=country,city=city,zip_code=zip_code,state=state)
                else:
                    update_address = Shipping_address(user_id = User(id=customer_id)
                    ,address=address,country=country,city=city,zip_code=zip_code,state=state)
                    update_address.save()
                return JsonResponse({'error_massage': error_massage,
                                     'url':'/my-account',
                                     'success': True})


        elif value == 'update_account':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            if not first_name:
                error_massage = "First Name Required !!"
            elif not last_name:
                error_massage = "Last Name Required !!"
            elif not phone:
                error_massage = "Phone Number Required !!"
            elif len(phone)<11:
                error_massage = "Phone Number Not Valid !!"
            elif not email:
                error_massage = "Email Required !!"
            elif re.match("^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", email) == None:
                error_massage = "Email Not Valid !!"
            if error_massage:

                return JsonResponse({'error_massage': error_massage,
                                     'url':'/my-account',
                                     'success': False})
            else:
                update_account = User.objects.filter(id = customer_id).update(first_name=first_name,
                last_name=last_name,phone=phone,email=email)
                return JsonResponse({'error_massage': error_massage,
                                     'url':'/my-account',
                                     'success': True})

        elif value == 'change_pass':
            password_u = request.POST.get('password')
            c_password = request.POST.get('n_password')
            n_password = request.POST.get('c_passwod')
            user = User.objects.get(id = customer_id)
            flag = check_password(password_u, user.password)

            if not password_u:
                error_massage = "Current Password Required !!"
            elif not c_password:
                error_massage = "New Password Required !!"
            elif not n_password:
                error_massage = "Confirm Password Required !!"
            elif c_password != n_password:
                error_massage = "New Password And Confirm Password Not Match !!"
            elif not flag:
                error_massage = "Your Resend Password Invalid !!"
            
            
            if error_massage:
                return JsonResponse({'error_massage': error_massage,
                                     'url':'/my-account',
                                     'success': False})
            else:
                update_account = User.objects.filter(id = customer_id).update(password = make_password(c_password))
                return JsonResponse({'error_massage': error_massage,
                                     'url':'/my-account',
                                     'success': True})

            

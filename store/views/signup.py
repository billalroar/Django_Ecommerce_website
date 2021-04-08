from django.views import View
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.brand import Brand
from store.models.product import Product
from store.models.user import User
import re
from store.models.category import Category





class Signup(View):

    return_url=[];

    def get(self, request):
        # Signup.return_url = request.GET.get('return_url')
        returnur1 = request.build_absolute_uri()
        Signup.return_url= returnur1.split('/')
        # print("FORM SIGNUP PAGE")
        # print(Signup.return_url)
        return render(request, 'login.html')
    def post(self, request):
        action = request.POST.get('action')
        if action == 'login':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.get_user_by_email(email)
            error_massage = None
            if user:
                flag = check_password(password, user.password)
                if flag:
                    request.session['customer_id'] = user.id

                    if Signup.return_url:
                        return HttpResponseRedirect('/'+Signup.return_url[-1])
                    else:
                        Signup.return_url=None
                        return redirect('homepage')
                else:
                    error_massage = 'email or password invalid !!'
            else:
               error_massage = 'email or password invalid !!'
            return render(request, 'login.html', {'error1': error_massage})
        else:
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            phone = request.POST.get('phone')
            user = User(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password1)

            value = {
                'first_name' : first_name,
                'last_name' : last_name,
                'phone' : phone,
                'email' : email
            }
            error_message = None

            if not first_name:
                error_message = "First Name Required !!"
            elif len(first_name) < 4:
                error_message = "First name len must be 4"
            elif (not last_name):
                error_message = "Last Name Required !!"
            elif len(last_name) < 4:
                error_message = "Last name len must be 4"
            elif (not phone):
                error_message = "Phone Number Required !!"
            elif len(phone) < 11:
                error_message = "Phone Number len must be 11"
            elif (not email):
                error_message = "Email Required !!"
            elif re.match("^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", email) != None:
                error_message = "Email not valid"
            elif (not password1):
                error_message = "PassWord Required !!"
            elif len(password1) < 6:
                error_message = "Password len must be 6"
            elif (not password2):
                error_message = "RepassWord Required !!"
            elif len(password2) < 6:
                error_message = "repassword len must be 6"
            elif password1 != password2:
                error_message = "Password not match !!"
            elif user.isExists():
                error_message = 'Email Allready Exists'

            # validation end
            if not error_message:
                user.password = make_password(user.password)
                user.register()
                return redirect('signuppage')
            else:
                data = {
                    'error': error_message,
                    'values': value
                }
                return render(request, 'login.html',data)

def logout(request):
    request.session['customer_id']=None
    return redirect('signuppage')
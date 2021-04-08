from django.views import View
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render,redirect
from store.models.user import User
from store.models.contact import Contact
import re



class Contactpage(View):

    def get(self, request):
        return render(request, 'contact.html' )
    
    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        error_message = None
        value = {
                'name' : name,
                'email' : email,
                'subject' : subject,
                'message' : message
            }

        if not name:
            error_message = "Name Required !!"
        elif len(name) < 4:
            error_message = "name len must be 4"
        elif (not email):
            error_message = "email Required !!"
        elif len(email) < 7:
            error_message = "email not valid !!"
        elif re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) == None:
            error_message = "email not valid !!"
        elif (not subject):
            error_message = "subject Required !!"
        elif (not message):
            error_message = "message Required !!"
        else:  
            message_send = Contact(name=name,email=email,subject=subject,message=message)
            message_send.register()
        if not error_message:
                return redirect('contactpage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
        return render(request, 'contact.html',data)
        

from django.shortcuts import redirect

def auth_middleware(get_response):



    def middleware(request):
        returnurl = request.META.get('PATH_INFO', None)
        returnur1 = request.build_absolute_uri()
        # returnur2 = request.build_absolute_uri('?')
        # returnur3 = request.build_absolute_uri('/')[:1].strip("/")
        # returnur4 = request.build_absolute_uri('/').strip("/")
        # print(returnurl)
        # print(returnur1)
        # print(returnur2)
        # print(returnur3)
        # print(returnur4)
        n_path= returnur1.split('/')
        # print(n_path[-1])
        if not request.session.get('customer_id'):
            # print("MIDDKLEWARE : "+returnur1)
            return redirect(f'/signup?return_url=/{n_path[-1]}')
        else:
            pass
        response = get_response(request)
        # print(response)
        return response
    

    return middleware
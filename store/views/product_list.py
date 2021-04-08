from django.views import View
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render,redirect
from store.models.brand import Brand
from store.models.product import Product
from store.models.user import User
from django.core.paginator import Paginator



class Product_list(View):

    def get(self, request):
        dic ={}
        cart_product = request.GET.get('cart')
        wishlist_product = request.GET.get('wishlist')
        search_product = request.GET.get('search')
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
        elif search_product:
           request.session['product_view_id'] = search_product
           return redirect('product_detailspage')
        brands = Brand.get_all_brand();
        b={}
        if brands:
            for n in brands:
                b[str(n)]=str(len(Product.objects.filter(brand = n)))
            dic['br']=b     
        for i in b:
            print(i+ ":" +b[i])
        categoryID = request.GET.get('category')
        search_text = request.GET.get('search_text')
        brand_search = request.GET.get('brand_search')
        alert = None
        if categoryID !="None" and categoryID!='' and categoryID !=None:
             print(categoryID)
             product_all = Product.get_all_product_by_category_id(categoryID)
             search_text = ''
        elif search_text !='' and search_text != "None" and search_text != None:
            product_all = Product.objects.filter(name__icontains=search_text)
            if list(product_all) == []:
                alert = 'Not found anything'
        elif brand_search !='' and brand_search != "None" and brand_search != None:
            print("brand search")
            print(brand_search)
            brand_id = Brand.objects.values_list('id').get(name = brand_search)
            print(brand_id)
            product_all = Product.objects.filter(brand = brand_id)
            print(product_all)
        else:
            product_all = Product.objects.all();
            categoryID = ''
            search_text = ''
        product_paginator = Paginator(product_all, 9)
        page_num = request.GET.get('page')
        product_page =product_paginator.num_pages
        
        page = []
        
        if not page_num:
            page_num = 1
        product = product_paginator.get_page(page_num)

        if 1<int(page_num) and int(page_num)<product_page: 
            page.append(int(page_num)-1)
            page.append(int(page_num))
            page.append(int(page_num)+1)
        else:
            if 1 == int(page_num) and product_page >2:
                page.append(int(page_num))
                page.append(int(page_num)+1)
                page.append(int(page_num)+2)
            elif product_page == int(page_num) and product_page>2:
                page.append(int(page_num)-2)
                page.append(int(page_num)-1)
                page.append(int(page_num))
            elif int(page_num)<product_page and product_page >1:
                page.append(int(page_num))
                page.append(int(page_num)+1)
            elif int(page_num)==product_page and product_page >1:
                page.append(int(page_num)-1)
                page.append(int(page_num))   
            else:
                if alert == None:
                    page.append(int(page_num))
                else:
                    dic['alert'] = alert
                
                
        dic['brands'] = brands
        dic['search_text'] = search_text
        dic['brand_search'] = brand_search
        dic['page'] = page
        dic['resendpage'] = int(page_num)
        dic['first_10_product'] = product
        dic['categoryID'] = categoryID
        dic['all_product'] = Product.get_all_product()
        return render(request, 'product-list.html' , dic)
    


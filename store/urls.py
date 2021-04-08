from django.contrib import admin
from django.urls import path
from .views import index,product_list,signup,cart,wishlist,product_details,contact,checkout,myaccount
from .views.signup import logout
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

urlpatterns = [
    path('', index.Index.as_view(), name='homepage'),
    path('product-list', product_list.Product_list.as_view(),name='productlistpage'),
    path('signup', signup.Signup.as_view(),name='signuppage'),
    path('logout', logout, name='logout'),
    path('cart', cart.Cart.as_view(), name='cartpage'),
    path('wishlist', wishlist.Wishlist.as_view(), name='wishlistpage'),
    path('product-detail', product_details.Product_detail.as_view(), name='product_detailspage'),
    path('contact', contact.Contactpage.as_view(), name='contactpage'),
    path('checkout', auth_middleware(checkout.Checkout.as_view()), name='checkoutpage'),
    path('my-account', myaccount.Myaccount.as_view(), name='myaccountpage'),
]

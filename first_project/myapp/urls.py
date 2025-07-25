
from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
    path("",views.index,name='index'),
    path("about.html",views.about,name='about'),
    path("contact.html",views.contact,name='contact'),
    path('login.html',views.login,name='login'),
    path('image1.html',views.image1,name='image1'),
    path('signup.html',views.signup,name='signup'),
    path('buynow.html',views.buynow,name='buynow'),
    path('cart.html',views.cart,name='cart'),
    path('logout.html',views.logout,name='logout')
    
]

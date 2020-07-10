
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
path('cart/', views.cartView, name='cartView'),
path('cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
path('cartRemove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),

]
 

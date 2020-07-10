
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

path('checkout/', views.checkout, name='checkout'),
path('orders/', views.order, name='user_order'),
]
 

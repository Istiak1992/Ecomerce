from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [

    path('', views.home, name='home'),
    path('s/', views.search, name='search'),
    
    path('products/', views.productlist, name='productlist'),
    path('products/<int:pk>/', views.ProductDetailView, name='singleproduct'),
]
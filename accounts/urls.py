
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

path('logout/', views.logout_view, name='logout_view'),
path('login/', views.login_view, name='login_view'),
path('registration/', views.registration_view, name='registration_view'),
path('accounts/activate/<str:activation_key>/', views.activation_view, name='activation_view'),



]
 

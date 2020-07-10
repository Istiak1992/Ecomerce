from django.urls import path
from . import views


urlpatterns = [
    
path('dismiss_marketing_message/', views.dismiss_marketing_message, name='dismiss_marketing_message_view'),

]

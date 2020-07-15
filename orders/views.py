import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from carts.models import Cart
from .models import *
from .utils import id_generator
from accounts.forms import UserAddressForm 
from accounts.models import UserAddress
from django.conf import settings

try:
	stripe_pub =settings.STRIPE_PUBLISHABLE_KEY
except:
	stripe_pub = "pk_test_giqz4Y9dhjdg6QtIUbuOBahj"

def order(request):
	context = {}
	template = 'orders/user.html'
	return render(request, template, context)

@login_required
def checkout(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
		return HttpResponseRedirect(reverse('cartView'))
	try:
		 new_order = Order.objects.get(cart = cart)
	except Order.DoesNotExist:
		new_order = Order()
		new_order.cart=cart
		new_order.user = request.user
		new_order.order_id = id_generator()
		new_order.save()
	except:
		return HttpResponseRedirect(reverse('cartView'))

	try:
		address_added = request.GET.get("address_added")
	except:
		address_added = None
	if address_added is None:
		address_form = UserAddressForm()
	else:
		address_form = None
	current_addresses = UserAddress.objects.filter(user=request.user)
	billing_addresses = UserAddress.objects.get_billing_addresses(user=request.user)

	if new_order.status == "Finished":
		#cart.delete()
		del request.session['cart_id']
		del request.session['items_total']
		return HttpResponseRedirect(reverse('cartView'))
		
	context = {'address_form': address_form, 'current_addresses':current_addresses, 
	'billing_addresses':billing_addresses, 'stripe_pub':stripe_pub,}
	template = 'orders/checkout.html'
	return render(request, template, context)

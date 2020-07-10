import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from carts.models import Cart
from .models import *
from .utils import id_generator
from accounts.forms import UserAddressForm 
from accounts.models import UserAddress

# Create your views here.
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

	address_form = UserAddressForm(request.POST or None)
	if address_form.is_valid():
		new_address = address_form.save(commit=False)
		new_address.user = request.user
		new_address.save()

	if new_order.status == "Finished":
		#cart.delete()
		del request.session['cart_id']
		del request.session['items_total']
		return HttpResponseRedirect(reverse('cartView'))
		
	context = {'address_form': address_form,}
	template = 'orders/checkout.html'
	return render(request, template, context)

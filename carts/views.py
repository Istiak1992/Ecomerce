from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from products.models import Product, Variation
# Create your views here.

def cartView(request):
	try:
		the_id = request.session['cart_id']
	except:
		the_id = None
	if the_id:
		cart = Cart.objects.get(id=the_id)
		new_total = 0.00
		for item in cart.cartitem_set.all():
			line_total = float(item.product.sales_price) * item.quantity

			new_total += line_total

		request.session['items_total'] = cart.cartitem_set.count()

		cart.total = new_total
		cart.save()
		context = {'cart':cart,}
	else:
		empty_message = 'Your cart is empty. Please keep shopping.'
		context = {'empty':True, 'empty_message':empty_message}
	template = 'carts/cartView.html'
	return render(request, template, context)

def remove_from_cart(request, id):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		return HttpResponseRedirect(reverse('cartView'))

	cartitem = CartItem.objects.get(id=id)
	cartitem.delete()
	#cartitem.cart = None
	#cartitem.save()
	return HttpResponseRedirect(reverse('cartView'))
		
		

def add_to_cart(request, pk):
	request.session.set_expiry(120000)

	try:
		the_id = request.session['cart_id']

	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = request.session['cart_id']
	cart = Cart.objects.get(id = the_id)	

	try:
		product = Product.objects.get(id=pk)

	except Product.DoesNotExist:
		pass
	except:
		pass
	
	product_variations = []
	if request.method=='POST':
		qty = request.POST['qty']
		for item in request.POST:
			key = item
			val = request.POST[key]
			try:
				v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
				product_variations.append(v)
			except:
				pass


		cart_item = CartItem.objects.create(cart=cart, product=product)

		if len(product_variations)>0:
			cart_item.variations.add(*product_variations)
		cart_item.quantity = qty
		cart_item.save()

		return HttpResponseRedirect(reverse('cartView'))
	return HttpResponseRedirect(reverse('cartView'))


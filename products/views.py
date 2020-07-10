from django.shortcuts import HttpResponse, render
from .models import * 
from django.views.generic import DetailView
from marketing.models import MarketingMessage, Slider
# Create your views here.

def home(request):
	title = 'Home'
	sliders = Slider.objects.all_featured()
	products = Product.objects.all()
	marketing_message = MarketingMessage.objects.all()[0]
	context = {'products':products, 'title':title, 'marketing_message':marketing_message, 'sliders': sliders,}


	return render(request, 'products/home.html', context)

def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		product = Product.objects.filter(title__icontains=q)
		context = {'query':q, 'product': product}
		template = 'products/results.html'
	else:
		context = {}
		template = 'products/home.html'


	return render(request, template, context)

def productlist(request):
	products = Product.objects.all()
	context = {'products':products}

	return render(request, 'products/productlist.html', context)

def ProductDetailView(request,pk):
	try:
		product = Product.objects.get(id=pk)
		img = ProductImage.objects.filter(product=product)
		context = {'product': product,'img':img,}

		return render(request, 'products/single.html', context)
	except: 
		return HttpResponse('Oops... Product is not exist. Please enter correct product id.')



	
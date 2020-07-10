import re
from django.shortcuts import render, HttpResponseRedirect, Http404, reverse
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from .models import *

# Create your views here.

def logout_view(request):
	logout(request)
	messages.success(request, "successfully Loggedout. Feel free to login  again.")
	return HttpResponseRedirect(reverse('login_view'))

def login_view(request):
	btn = 'Login'
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username,password=password)
		login(request,user)
		messages.success(request, "successfully Loggedin. Welcome Back!")
		return HttpResponseRedirect('/')
		
	context = {'form':form, 'btn':btn,}
	return render(request, 'accounts/form.html', context)

def registration_view(request):
	btn = 'Join'
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		new_user = form.save(commit=False)
		#new_user.first_name = 'Justin'
		new_user.save()
		messages.success(request, "successfully Registered. Please check your email for confirmation.")
		return HttpResponseRedirect('/')
	context = {'form':form, 'btn':btn,}
	return render(request, 'accounts/form.html', context)

SHA1_RE = re.compile('^[a-f0-9]{40}$')

def activation_view(request, activation_key):
	if SHA1_RE.search(activation_key):
		print('Activation key is real.')
		try:
			instance = EmailConfirmed.objects.get(activation_key=activation_key)
		except EmailConfirmed.DoesNotExist:
			instance = None
			raise Http404
		if instance is not None and not instance.confirmed:
			page_message = 'Confirmation successful! Welcome.'
			instance.activation_key = "Confirmed"
			instance.confirmed = True
			instance.save()
		elif instance is not None and instance.confirmed:
			page_message = 'Already Confirmed'
		else:
			page_message = ""

		context = {'page_message': page_message}
		return render(request, 'accounts/activation_complete.html', context)
	else:
		raise Http404
from django.db import models
from django.conf import settings
import stripe
import random
import hashlib
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.shortcuts import reverse
from localflavor.us.us_states import US_STATES
from localflavor.se.se_counties import COUNTY_CHOICES


class UserAddress(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	address = models.CharField(max_length=120)
	address2 = models.CharField(max_length=120, null=True, blank=True)
	city = models.CharField(max_length=120)
	state = models.CharField(max_length=120, choices=COUNTY_CHOICES)
	country = models.CharField(max_length=120)
	zipcode = models.CharField(max_length=120)
	phone = models.CharField(max_length=120)
	shipping = models.BooleanField(default=True)
	billing = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return str(self.user.username)

stripe.api_key = settings.STRIPE_SECRET_KEY

User =get_user_model()

class UserStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	stripe_id = models.CharField(max_length=120, null=True, blank=True)

	def __str__(self):
		return str(self.stripe_id)

class EmailConfirmed(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	activation_key = models.CharField(max_length=200)
	confirmed = models.BooleanField(default=False)

	def __str__(self):
		return str(self.confirmed)
	def active_user_email(self):
		activationUrl = "%s%s"  %(settings.SITE_URL, reverse('activation_view', args=[self.activation_key]))
		context = {
			"activationKey": self.activation_key,
			"activationUrl": activationUrl,
			"user": self.user.username,
		}
		subject = "Activate your email"
		message = render_to_string("accounts/activation_message.txt",context)
		self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
		
	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject,message,from_email,[self.user.email], kwargs)

def get_create_stripe(user):
	new_user_stripe, created = UserStripe.objects.get_or_create(user=user)
	if created:
		customer = stripe.Customer.create(
			email = user.email
			)
		new_user_stripe.stripe_id = customer.stripe_id
		new_user_stripe.save()
	

def user_created(sender, instance, created, *args, **kwargs):
	user = instance
	if created:
		get_create_stripe(user)
		email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user=user)
		if email_is_created:
			short_hash = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
			base,domain = str(user.email).split("@")
			activation_key = hashlib.sha1((short_hash+base).encode('utf-8')).hexdigest()
			email_confirmed.activation_key =activation_key
			email_confirmed.save()
			email_confirmed.active_user_email()

post_save.connect(user_created, sender=User)



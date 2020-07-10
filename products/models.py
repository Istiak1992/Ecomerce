from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length = 120)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	sales_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title
	class Meta:
		unique_together = ('title', 'slug')

	

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True)
	feature = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	thumbnail = models.BooleanField(default=False)

	def __str__(self):
		return self.product.title

class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)
	def sizes(self):
		return self.all().filter(category='size')
	def colors(self):
		return self.all().filter(category='color')

VAR_CATEGORIES = (
	('size', 'size'),
	('color', 'color'),
	('package', 'package'),
	)

class Variation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
	image = models.ForeignKey(ProductImage, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=120)
	price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	objects = VariationManager()

	def __str__(self):
		return self.title
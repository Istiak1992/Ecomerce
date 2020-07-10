from django.contrib import admin
from .models import UserStripe, EmailConfirmed, UserAddress

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
	class Meta:
		model = UserAddress

admin.site.register(UserAddress, UserModelAdmin)
admin.site.register(UserStripe)
admin.site.register(EmailConfirmed)

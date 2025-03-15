from django.contrib import admin # type: ignore
from .models import Cart, Customer, Menu,Restaurants

# Register your models here.
admin.site.register(Customer)
admin.site.register(Restaurants)
admin.site.register(Menu)
admin.site.register(Cart)

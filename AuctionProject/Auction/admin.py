from django.contrib import admin
from .models import Product , Customer
# Register your models here.

@admin.register(Product)


class RegisterProduct(admin.ModelAdmin):
    list_display = ('ProductName','ProductImage','DateTime','Description')

@admin.register(Customer)

class RegisterCustomer(admin.ModelAdmin):
    list_display = ('UserName','FirstName','LastName','MobileNo','EmailId','Password')
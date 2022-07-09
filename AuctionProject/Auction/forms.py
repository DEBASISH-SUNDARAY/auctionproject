from dataclasses import fields
from django import forms
from .models import Product

class AddProduct(forms.ModelForm):
    class Meta:
        model=Product
        fields=["ProductName","ProductImage","DateTime","Description"]

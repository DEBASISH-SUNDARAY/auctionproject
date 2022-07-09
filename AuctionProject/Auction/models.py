from email.headerregistry import UniqueSingleAddressHeader
from django.db import models

# Create your models here.
class Product(models.Model):
    ProductName = models.CharField(max_length=20)
    ProductImage = models.ImageField(upload_to="productImage")
    DateTime = models.CharField( max_length=50)
    Description = models.CharField(max_length=300)

class Customer(models.Model):
    UserName=models.CharField(max_length=30)
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    MobileNo=models.CharField(max_length=15)
    EmailId=models.CharField(max_length=50)
    Password=models.CharField(max_length=30)

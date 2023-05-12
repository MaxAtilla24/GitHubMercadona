from django.db import models

# Create your models here.
class Product (models.Model):
    productName = models.CharField(max_length=200)
    productDescr = models.TextField()
    productCategory = models.SmallIntegerField()
    productPriceBase = models.DecimalField(max_digits=6, decimal_places=2)
    productdiscount = models.DecimalField(max_digits=4, decimal_places=2)
    productimage = models.CharField(max_length= 200)
    

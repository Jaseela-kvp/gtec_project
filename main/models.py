from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/product/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    # brand = models.CharField(max_length=100)
    description = models.TextField()
    # color = models
    # size = 

    def __str__(self):
        return self.name
 


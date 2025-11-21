from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)

    stock_keeping_unit = models.CharField(max_length=100, unique=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")

    image_url = models.URLField(max_length=500, blank=True, null=True)

    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
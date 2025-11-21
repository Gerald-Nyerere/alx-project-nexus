from django.db import models
from orders.models import Order
from products.models import Product

# Create your models here.
class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items'
    )

    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity} (Order #{self.order.order_number})"

    def save(self, *args, **kwargs):
        # Automatically calculate subtotal
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)

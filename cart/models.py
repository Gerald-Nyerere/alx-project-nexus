from django.db import models
from django.conf import settings

# Create your models here.
class ShoppingCart(models.Model):
    cart_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="shopping_carts")

    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.cart_id} - {self.user.email}"

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True, related_name="items")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name="cart_items")

    quantity = models.PositiveIntegerField(default=1)

    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cart.user.email} - {self.product.name} (x{self.quantity})"

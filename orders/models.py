from django.db import models
from django.conf import settings

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)

    # FK to your custom user model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')

    order_number = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.order_number} - {self.user.email}"
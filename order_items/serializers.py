from rest_framework import serializers
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    order_number = serializers.ReadOnlyField(source='order.order_number')

    class Meta:
        model = OrderItem
        fields = [
            'order',
            'order_number',
            'product',
            'product_name',
            'quantity',
            'unit_price',
            'subtotal',
        ]

    def create(self, validated_data):
        # subtotal will be auto-calculated in model's save()
        return super().create(validated_data)

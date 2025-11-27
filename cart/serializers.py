from rest_framework import serializers
from .models import ShoppingCart, CartItem
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)  # nested product info

    class Meta:
        model = CartItem
        fields = [
            'id',
            'product',
            'product_detail',
            'quantity',
            'added_at',
        ]

class ShoppingCartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)  # nested items in the cart

    class Meta:
        model = ShoppingCart
        fields = ['cart_id', 'user', 'items', 'created_at']

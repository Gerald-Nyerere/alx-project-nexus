from django.shortcuts import render
from rest_framework import viewsets
from .models import CartItem, ShoppingCart
from .serializers import CartItemSerializer, ShoppingCartSerializer

# Create your views here.
class ShoppingCartViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing shopping carts.
    """
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing items in a shopping cart.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
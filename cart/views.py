from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from users.permissions import IsAdmin, IsCustomer
from .models import CartItem, ShoppingCart
from .serializers import CartItemSerializer, ShoppingCartSerializer

# Create your views here.
class ShoppingCartViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing shopping carts.
    """
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    
    #permisions to differnt users
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]  
        elif self.action == 'create':
            return [IsCustomer()]  
        elif self.action in ['update', 'partial_update']:
            return [IsCustomer()]  
        elif self.action == 'destroy':
            return [IsCustomer()]  
        return [IsAuthenticated()]

class CartItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing items in a shopping cart.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
    #permisions to differnt users
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        elif self.action == 'create':
            return [IsCustomer()]
        elif self.action in ['update', 'partial_update']:
            return [IsCustomer()]
        elif self.action == 'destroy':
            return [IsCustomer()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        # Get or create the cart for the logged-in user
        cart, _ = ShoppingCart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsCustomer, IsVendor
from .models import OrderItem
from .serializers import OrderItemSerializer

# Create your views here.
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]  
        elif self.action == 'create':
            return [IsCustomer()] 
        elif self.action in ['update', 'partial_update']:
            return [IsCustomer(), IsVendor()] 
        elif self.action == 'destroy':
            return [IsAdmin()]  
        return [IsAuthenticated()]
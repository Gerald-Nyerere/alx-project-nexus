from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsCustomer, IsAdmin, IsVendor
from .models import Order
from .serializers import OrderSerializer

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        elif self.action == 'create':
            return [IsCustomer()]
        elif self.action in ['update', 'partial_update']:
            return [IsVendor()]
        elif self.action == 'destroy':
            return [IsAdmin()]
        return [IsAuthenticated()]
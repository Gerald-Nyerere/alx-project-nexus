from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsCustomer, IsAdmin, IsVendor
from .models import Order
from .filters import OrderFilter
from .serializers import OrderSerializer

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    filterset_class = OrderFilter

    # Admin search
    search_fields = ["order_number", "user__email"]

    # Sorting
    ordering_fields = ["order_date", "total_amount"]
    ordering = ["-order_date"]

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
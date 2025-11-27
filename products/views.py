from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsVendor
from .serializers import ProductSerializer
from .filters import ProductFilter
from .models import Product


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Enable filtering, ordering, and search
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = ProductFilter
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at'] 
    search_fields = ['name']

    # Enable permission to users
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        
        elif self.action == 'create':
            return [IsVendor()]


        elif self.action in ['update', 'partial_update']:
            return [IsVendor()]

        elif self.action == 'destroy':
            return [IsAdmin()]

        return [IsAuthenticated()]
    

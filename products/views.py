from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsVendor
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

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
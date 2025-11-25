from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsManager
from .models import Category
from .serializers import CategorySerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]  
        elif self.action in ['create']:
            return [IsAdmin()]  
        elif self.action in ['update', 'partial_update']:
            return [IsManager()]  
        elif self.action == 'destroy':
            return [IsAdmin()]  
        return [IsAuthenticated()]
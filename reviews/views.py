from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsAdmin, IsCustomer, IsModerator
from .models import Review 
from .serializers import ReviewSerializer

# Create your views here.
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()] 
    
        elif self.action == 'create':
            return [IsCustomer()]  
        
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsCustomer(), IsModerator()] 
        
        elif self.action == 'destroy':
            return [IsModerator()]
        
        return [IsAuthenticated()]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShoppingCartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'', ShoppingCartViewSet, basename='carts')
router.register(r'cart-items', CartItemViewSet, basename='cart-items')

urlpatterns = [
    path('', include(router.urls)),
]

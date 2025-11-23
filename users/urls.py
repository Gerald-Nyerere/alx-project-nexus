from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  UserViewSet, UserProfileView, UserRegistration, UserLoginView

router = DefaultRouter()
router.register(r'',  UserViewSet, basename='users')

urlpatterns = [
    # Registration endpoint
    path('register/', UserRegistration.as_view(), name='user-register'),
    # Login endpoint
    path('login/', UserLoginView.as_view(), name='user-login'),
    # Profile endpoint (requires token)
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    # DRF ViewSet CRUD routes
    path('', include(router.urls)),
]

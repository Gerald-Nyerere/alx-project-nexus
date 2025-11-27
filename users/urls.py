from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import  UserViewSet, UserProfileView, UserRegistration

router = DefaultRouter()
router.register(r'',  UserViewSet, basename='users')

urlpatterns = [
     # JWT endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh access token

    # Registration endpoint
    path('register/', UserRegistration.as_view(), name='user-register'),

    # Profile endpoint (requires JWT access token)
    path('profile/', UserProfileView.as_view(), name='user-profile'),

    # DRF ViewSet CRUD routes
    path('', include(router.urls)),
]

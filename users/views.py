from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer

# Create your views here.

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 

    # Optional: only admin can list/delete users
    def get_permissions(self):
        if self.action in ['create']:  # Anyone can create
            return [AllowAny()]
        if self.action in ['destroy', 'list']:  # Only admin
            from rest_framework.permissions import IsAdminUser
            return [IsAdminUser()]
        return super().get_permissions()




# User Registration
class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Registration successful"}, status=status.HTTP_201_CREATED)



# User Login
class UserLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "detail": "Login successful",
                "token": token.key,
                "email": user.email
            }, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Profile
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
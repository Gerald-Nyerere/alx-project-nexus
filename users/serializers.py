from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    roles = serializers.ChoiceField(choices=User.ROLE_CHOICES, required=True)
    phone = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'roles', 'phone']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        # HASH PASSWORD
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            # HASH PASSWORD
            instance.set_password(password)
        instance.save()
        return instance

from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')  

    class Meta:
        model = Order
        fields = [
            'order_number',
            'user',
            'user_email',
            'order_date',
            'total_amount',
        ]

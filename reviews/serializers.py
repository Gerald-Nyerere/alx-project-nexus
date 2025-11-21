from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Review
        fields = [
            'user_email',
            'product_name',
            'product',
            'rating',
            'title',
            'comment',
        ]
        read_only_fields = ['review_id', 'user_email', 'product_name']
    
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        return Review.objects.create(user=user, **validated_data)

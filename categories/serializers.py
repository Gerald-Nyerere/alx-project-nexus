from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.ReadOnlyField(source='parent_category.name') 
    
    class Meta:
        model = Category
        fields = [
            'category_id',
            'name',
            'description',
            'parent_category',
            'parent_name',    
            'image_url',
            'is_active',
        ]

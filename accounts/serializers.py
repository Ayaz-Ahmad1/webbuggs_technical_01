# serializers.py
from rest_framework import serializers
from .models import User
from products.models import Product

class ProductCountSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'product_count']

    def get_product_count(self, obj):
        return obj.created_products.count() 
    

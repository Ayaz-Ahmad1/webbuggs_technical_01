from rest_framework import serializers
from .models import ProductCategory, SubCategory, Color, Product


#Get Product Category Serializer
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
 #       fields = '__all__'
        fields = ('id', 'name', 'short_name', 'image', 'description', 'is_active', 'created_by', 'updated_by', 'created_at', 'updated_at')

#Get Product Sub Category Serializer
class SubCategorySerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer( read_only = True)
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'short_name', 'image', 'description', 'is_active', 'created_by', 'updated_by', 'created_at', 'updated_at','category' )

#Add Product Sub Category Serializer
class NewSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'short_name', 'image', 'description', 'is_active', 'created_by', 'updated_by', 'created_at', 'updated_at','category' )



#Get Product-Color Serializer
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', 'color_code', 'created_at')


#Get Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'sku', 'is_active', 'created_by', 'updated_by', 'created_at', 'color','sub_category')

#Get Product Serializer
class GetProductSerializer(serializers.ModelSerializer):
    category = SubCategorySerializer( read_only = True)
    color = ColorSerializer(many=True, read_only = True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'sku', 'is_active', 'created_by', 'updated_by', 'created_at', 'color','category')




#Get Top 3 Category Serializer
class Top3CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
 #       fields = '__all__'
        fields = ('id', 'name', 'short_name')

#Get Top 3 SubCategory Serializer
class Top3SubCategorySerializer(serializers.ModelSerializer):
    category = Top3CategorySerializer( read_only = True)
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'short_name','is_active', 'category' )

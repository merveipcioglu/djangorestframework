from rest_framework import serializers
from .models import IHA, Brand, Model , Category

class IHACreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IHA
        fields = ['brand', 'model', 'category', 'weight']

class IHAUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IHA
        fields = ['id','brand', 'model', 'category', 'weight']

class IHAListSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    model_name = serializers.CharField(source='model.name')

    class Meta:
        model = IHA
        fields = ['id', 'weight', 'brand_name', 'category_name', 'model_name']

class IHADeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()        

# Brand  
    
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class BrandAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

class BrandDeleteSerializer(serializers.Serializer):

    id = serializers.IntegerField()          

# model

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'name']        

class ModelAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['name']

class ModelDeleteSerializer(serializers.Serializer):

    id = serializers.IntegerField()    

#Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']   
        

class CategoryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CategoryDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField() 
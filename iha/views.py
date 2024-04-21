from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import IHA, Brand , Model ,Category
from .serializers import IHACreateSerializer , IHAUpdateSerializer , IHAListSerializer , IHADeleteSerializer
from .serializers import BrandDeleteSerializer , BrandAddSerializer ,  BrandSerializer 
from .serializers import ModelAddSerializer , ModelDeleteSerializer , ModelSerializer
from .serializers import CategorySerializer , CategoryAddSerializer , CategoryDeleteSerializer
@api_view(['POST'])
def createIha(request):
    if request.method == 'POST':
        serializer = IHACreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def updateIha(request):
    if request.method == 'POST':
        serializer = IHAUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET'])
def listIha(request):
    if request.method == 'GET':
        ihas = IHA.objects.all()
        serializer = IHAListSerializer(ihas, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def deleteIha(request):
    if request.method == 'POST':
        serializer = IHADeleteSerializer(data=request.data)
        if serializer.is_valid():
            iha_id = serializer.validated_data['id']
            try:
                iha = IHA.objects.get(id=iha_id)
                iha.delete()
                return Response({'message': 'IHA deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            except IHA.DoesNotExist:
                return Response({'message': 'IHA not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

# Brand
@api_view(['GET'])
def listBrand(request):
    if request.method == 'GET':
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def deleteBrand(request):
    if request.method == 'POST':
        serializer = BrandDeleteSerializer(data=request.data)
        if serializer.is_valid():
            brand_id = serializer.validated_data['id']
            try:
                brand = Brand.objects.get(id=brand_id)
                brand.delete()
                return Response({'message': 'Brand deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            except Brand.DoesNotExist:
                return Response({'message': 'Brand not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['POST'])
def createBrand(request):
    if request.method == 'POST':
        serializer = BrandAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
#Model   
@api_view(['GET'])
def listModel(request):
    if request.method == 'GET':
        models = Model.objects.all()
        serializer = ModelSerializer(models, many=True)
        return Response(serializer.data)    

@api_view(['POST'])
def createModel(request):
    if request.method == 'POST':
        serializer = ModelAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
@api_view(['POST'])
def deleteModel(request):
    if request.method == 'POST':
        serializer = ModelDeleteSerializer(data=request.data)
        if serializer.is_valid():
            model_id = serializer.validated_data['id']
            try:
                model = Model.objects.get(id=model_id)
                model.delete()
                return Response({'message': 'Model deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            except Model.DoesNotExist:
                return Response({'message': 'Model not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
    
#Category
    
@api_view(['GET'])
def listCategory(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)     
    
@api_view(['POST'])
def createCategory(request):
    if request.method == 'POST':
        serializer = CategoryAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
@api_view(['POST'])
def deleteCategory(request):
    if request.method == 'POST':
        serializer = CategoryDeleteSerializer(data=request.data)
        if serializer.is_valid():
            category_id = serializer.validated_data['id']
            try:
                category = Category.objects.get(id=category_id)
                category.delete()
                return Response({'message': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            except Category.DoesNotExist:
                return Response({'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserRentIhaHistory , IHA
from .serializers import UserRentIhaHistorySerializer , UserRentIhaHistoryUpdateSerializer

@api_view(['POST'])
def rentIha(request):
    if request.method == 'POST':
        serializer = UserRentIhaHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Kullanıcı ve IHA nesnelerini kaydetmek için
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def deleteRentIha(request):
    if request.method == 'POST':
        try:
            id = request.data.get('id')
            rent_iha = UserRentIhaHistory.objects.get(id=id)
            rent_iha.delete()
            return Response({'message': 'Rent IHA deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except UserRentIhaHistory.DoesNotExist:
            return Response({'error': 'Rent IHA not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET'])
def listRentIhaByIhaId(request):
    if request.method == 'GET':
        iha_id = request.data.get('ihaId')
        if iha_id is not None:
            rent_iha_list = UserRentIhaHistory.objects.filter(iha_id=iha_id)
            serializer = UserRentIhaHistorySerializer(rent_iha_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ihaId must be provided in the request body'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
 
@api_view(['PUT'])
def updateRentIha(request, pk):
    try:
        rent_iha = UserRentIhaHistory.objects.get(pk=pk)
    except UserRentIhaHistory.DoesNotExist:
        return Response({'error': 'Rent IHA not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = UserRentIhaHistoryUpdateSerializer(rent_iha, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Fruit
from .serializers import FruitSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def fruit_view(request, pk = None, *args, **kwargs):

    if request.method == "POST":
        serializer = FruitSerializer(data = request.data)
        if serializer.is_valid():
            instance = serializer.save()
            response_serializer = FruitSerializer(instance)
            data = response_serializer.data
            return Response(data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

    if request.method == "GET":
        if pk:
            try:
                fruit = Fruit.objects.get(id = pk)
                serializer = FruitSerializer(fruit)
                return Response(serializer.data, status = status.HTTP_200_OK)
            except Fruit.DoesNotExist:
                return Response({"error": "Fruit not found"}, status = status.HTTP_404_NOT_FOUND)
        
        queryset = Fruit.objects.all()
        serializer = FruitSerializer(queryset, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)  


    if request.method == "PUT":
        if pk:
            try:
                fruit = Fruit.objects.get(id = pk)
                serializer = FruitSerializer(fruit, data = request.data, partial = True)
                if serializer.is_valid():
                    instance = serializer.save()
                    response_serializer = FruitSerializer(instance)
                    data = response_serializer.data
                    return Response(data, status = status.HTTP_200_OK)
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            except Fruit.DoesNotExist:
                return Response({"error": "Fruit not found"}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        if pk:
            instance = get_object_or_404(Fruit, id = pk)  
            instance.delete()
            return Response({"message": "fruit details deleted successfully"}, status = status.HTTP_204_NO_CONTENT)
            
        return Response({"error": "No id provided"}, status = status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Unsupported request method"}, status = status.HTTP_405_METHOD_NOT_ALLOWED)
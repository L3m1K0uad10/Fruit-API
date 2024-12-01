from rest_framework import generics

from .models import Fruit
from .serializers import FruitSerializer



class FruitListCreateAPIView(generics.ListCreateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer 


class FruitDetailAPIView(generics.RetrieveAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    lookup_field = "pk"


class FruitUpdateAPIView(generics.UpdateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer 
    lookup_field = "pk"


class FruitDestroyAPIView(generics.DestroyAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer 
    lookup_field = "pk"
from rest_framework import generics, permissions

from .models import Fruit
from .serializers import FruitSerializer



class FruitListCreateAPIView(generics.ListCreateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer 
    permission_classes = [permissions.AllowAny]


class FruitDetailAPIView(generics.RetrieveAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    lookup_field = "pk"
    permission_classes = [permissions.AllowAny]


class FruitUpdateAPIView(generics.UpdateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer 
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser]


class FruitDestroyAPIView(generics.DestroyAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer 
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser]
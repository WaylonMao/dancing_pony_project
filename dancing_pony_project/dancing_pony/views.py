from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Dish
from .serializers import DishSerializer
from rest_framework.permissions import IsAuthenticated


class DishListCreateView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]


class DishRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]

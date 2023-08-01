from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Dish
from .serializers import DishSerializer


class DishListCreateView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

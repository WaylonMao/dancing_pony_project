from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Dish
from .permissions import CanRateDish
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


class DishRatingView(generics.GenericAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated, CanRateDish]

    def post(self, request, pk):
        dish = self.get_object()
        user = request.user
        rating = request.data.get('rating')

        if not rating or not isinstance(rating, int) or rating < 1 or rating > 5:
            return Response({'error': 'Invalid rating value. Please provide a rating between 1 and 5.'},
                            status=status.HTTP_400_BAD_REQUEST)

        user_rating = next((item for item in dish.ratings if item['id'] == user.id), None)
        if user_rating:
            return Response({'error': 'You have already rated this dish.'}, status=status.HTTP_400_BAD_REQUEST)

        dish.ratings.append({'id': user.id, 'rating': rating})
        dish.rating = dish.calculate_average_rating()
        dish.save()

        return Response({'success': 'Dish rated successfully.'}, status=status.HTTP_200_OK)

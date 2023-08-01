from django.urls import path
from .views import DishListCreateView, DishRetrieveUpdateDestroyView, DishRatingView

urlpatterns = [
    path('dishes/', DishListCreateView.as_view(), name='dish-list-create'),
    path('dishes/<int:pk>/', DishRetrieveUpdateDestroyView.as_view(), name='dish-retrieve-update-destroy'),
    path('dishes/<int:pk>/rating/', DishRatingView.as_view(), name='dish-rating'),
]

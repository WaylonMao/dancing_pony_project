from django.urls import path
from .views import DishListCreateView, DishRetrieveUpdateDestroyView

urlpatterns = [
    path('dishes/', DishListCreateView.as_view(), name='dish-list-create'),
    path('dishes/<int:pk>/', DishRetrieveUpdateDestroyView.as_view(), name='dish-retrieve-update-destroy'),
]

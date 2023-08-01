from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Dish


class DishRatingAPITest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

        # Create a test dish
        self.dish = Dish.objects.create(name='Test Dish', description='Test description', price='9.99')

        # Set the rating endpoint URL
        self.url = reverse('dish-rating', args=[self.dish.id])

        # Authenticate the test user
        self.client.force_authenticate(user=self.user)

    def test_rating_endpoint_invalid_rating(self):
        # Make a POST request to the rating endpoint with an invalid rating (less than 1)
        data = {'rating': 0}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Invalid rating value. Please provide a rating between 1 and 5.'})

    def test_rating_endpoint_success(self):
        # Make a POST request to the rating endpoint with a valid rating (between 1 and 5)
        data = {'rating': 4}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'success': 'Dish rated successfully.'})

        # Refresh the dish object from the database
        self.dish.refresh_from_db()

        # Assert that the rating and ratings fields have been updated
        self.assertEqual(self.dish.rating, 4)
        self.assertEqual(self.dish.ratings, [{'id': self.user.id, 'rating': 4}])

    def test_rating_endpoint_user_already_rated(self):
        # Rate the dish two times
        self.client.post(self.url, {'rating': 4}, format='json')
        response = self.client.post(self.url, {'rating': 4}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'You have already rated this dish.'})

    def test_rating_endpoint_user_is_smeagol(self):
        # Set the test user's username to Sméagol
        self.user.username = 'Sméagol'
        self.user.save()

        response = self.client.post(self.url, {'rating': 4}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'You do not have permission to perform this action.'})

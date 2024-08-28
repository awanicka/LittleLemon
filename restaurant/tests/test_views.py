from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test data
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=100, inventory=50)
        Menu.objects.create(title="Burger", price=60, inventory=75)

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_getall(self):
        client = APIClient()
        # Authenticate the client
        client.force_authenticate(user=self.user)
        response = client.get(reverse('menu-items'))
        self.assertEqual(response.status_code, 200)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)

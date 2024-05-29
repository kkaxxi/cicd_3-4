from django.test import TestCase
from .models import MenuItem

class MenuItemTestCase(TestCase):
    def setUp(self):
        MenuItem.objects.create(name="Test Item", description="Test Description", price=9.99, available=True)

    def test_menu_item_creation(self):
        item = MenuItem.objects.get(name="Test Item")
        self.assertEqual(item.description, "Test Description")
        self.assertEqual(item.price, 9.99)
        self.assertTrue(item.available)

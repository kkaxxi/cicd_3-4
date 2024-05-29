from django.test import TestCase
from .models import ContactMessage

class ContactMessageTestCase(TestCase):
    def setUp(self):
        ContactMessage.objects.create(name="Test User", email="test@example.com", message="Test message")

    def test_contact_message_creation(self):
        message = ContactMessage.objects.get(name="Test User")
        self.assertEqual(message.email, "test@example.com")
        self.assertEqual(message.message, "Test message")

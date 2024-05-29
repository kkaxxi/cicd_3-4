from django.test import TestCase
from .models import About

class AboutTestCase(TestCase):
    def setUp(self):
        About.objects.create(title="Test Title", content="Test Content")

    def test_about_creation(self):
        about = About.objects.get(title="Test Title")
        self.assertEqual(about.content, "Test Content")

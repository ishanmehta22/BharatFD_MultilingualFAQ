import pytest
from django.test import TestCase, override_settings
from django.urls import reverse
from django.core.cache import cache
from faq.models import FAQ

pytestmark = pytest.mark.django_db

@override_settings(
    CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
        }
    }
)
class FAQAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faq = FAQ.objects.create(
            question='Test Question',
            answer='Test Answer'
        )
    
    def setUp(self):
        cache.clear()
    
    def test_api_response(self):
        url = reverse('faq-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertTrue(len(data) > 0)
        self.assertEqual(data[0]['question'], 'Test Question')
        
    def test_api_response_with_language(self):
        url = reverse('faq-list') + '?lang=hi'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertTrue(len(data) > 0)
        self.assertNotEqual(data[0]['question'], 'Test Question')  # Should be translated
        
    def test_cache_functionality(self):
        url = reverse('faq-list')
        
        # First request - should cache the response
        response1 = self.client.get(url)
        self.assertEqual(response1.status_code, 200)
        
        # Second request - should use cached response
        response2 = self.client.get(url)
        self.assertEqual(response2.status_code, 200)
        
        # Responses should be identical
        self.assertEqual(response1.json(), response2.json())
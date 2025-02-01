# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from django.utils.translation import gettext as _
from .models import FAQ
import logging

logger = logging.getLogger(__name__)

class FAQAPIView(APIView):
    def get_cached_data(self, language, faqs):
        """Helper method to get or generate cached data"""
        data = []
        for faq in faqs:
            if language in ['hi', 'bn'] and hasattr(faq, f'question_{language}'):
                question = getattr(faq, f'question_{language}')
            else:
                question = faq.question
                
            # Get translated answer
            try:
                translated_data = faq.translate_text(language)
                answer = translated_data['answer']
            except Exception as e:
                logger.error(f"Translation error: {e}")
                answer = faq.answer
                
            data.append({
                'question': question,
                'answer': answer,
            })
        return data

    def get(self, request):
        language = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        cache_key = f'faqs_{language}'
        
        try:
            # Try to get data from cache
            data = cache.get(cache_key)
            if data is None:
                # Cache miss, generate new data
                data = self.get_cached_data(language, faqs)
                cache.set(cache_key, data, timeout=3600)
        except Exception as e:
            # Handle any cache-related errors
            logger.error(f"Cache error: {e}")
            data = self.get_cached_data(language, faqs)
        
        return Response(data)
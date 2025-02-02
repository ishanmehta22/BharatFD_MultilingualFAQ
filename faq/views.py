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
            try:
                # Always use dynamic translation for consistency
                translated_data = faq.translate_text(language)
                
                data.append({
                    'question': translated_data['question'],
                    'answer': translated_data['answer'],
                })
            except Exception as e:
                logger.error(f"Translation error for FAQ {faq.id}: {e}")
                # Fallback to original text if translation fails
                data.append({
                    'question': faq.question,
                    'answer': faq.answer,
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
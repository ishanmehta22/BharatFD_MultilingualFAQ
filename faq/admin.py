from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'question_hi', 'question_bn']
    search_fields = ['question', 'question_hi', 'question_bn']
    readonly_fields = ['question_hi', 'question_bn']  # These are auto-generated

admin.site.register(FAQ, FAQAdmin)
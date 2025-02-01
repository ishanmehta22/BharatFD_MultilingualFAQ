from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation

    def save(self, *args, **kwargs):
        # Automatically translate when saving if translations are empty
        if not self.question_hi:
            translator = Translator()
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            translator = Translator()
            self.question_bn = translator.translate(self.question, dest='bn').text
        super().save(*args, **kwargs)

    def translate_text(self, language_code):
        """
        Dynamically translates the question and answer into the selected language.
        """
        translator = Translator()
        translated_question = translator.translate(self.question, dest=language_code).text
        translated_answer = translator.translate(self.answer, dest=language_code).text
        return {'question': translated_question, 'answer': translated_answer}

    def __str__(self):
        return self.question
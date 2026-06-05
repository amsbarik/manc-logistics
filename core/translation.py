from modeltranslation.translator import register, TranslationOptions
from .models import WhyChooseUs


@register(WhyChooseUs)
class WhyChooseUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
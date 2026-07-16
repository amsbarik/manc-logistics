from modeltranslation.translator import register, TranslationOptions

from .models import RiderRecruitment


@register(RiderRecruitment)
class RiderRecruitmentTranslationOptions(TranslationOptions):
    fields = ('heading', 'short_description', 'with_car_txt', 'without_car_txt')






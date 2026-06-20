from modeltranslation.translator import register, TranslationOptions

from .models import HeroSlider, LeadershipMessage, WhyChooseUs, FAQ, SiteSetting, City


@register(HeroSlider)
class HeroSliderTranslationOptions(TranslationOptions):
    fields = ('heading', 'short_description', 'cta_message', 'primary_btn_txt', 'secondary_btn_txt')


@register(LeadershipMessage)
class LeadershipMessageTranslationOptions(TranslationOptions):
    fields = ('heading', 'name', 'designation', 'message_01', 'message_02')


@register(WhyChooseUs)
class WhyChooseUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(SiteSetting)
class SiteSettingTranslationOptions(TranslationOptions):
    fields = ('mobile_sale', 'mobile_support', 'address', 'about_company', 'office_hours')












from modeltranslation.translator import register, TranslationOptions

from .models import FoodCategory, VendorBranch


@register(FoodCategory)
class FoodCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(VendorBranch)
class VendorBranchTranslationOptions(TranslationOptions):
    fields = ('branch_name', 'short_description', 'address')







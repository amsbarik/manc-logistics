
from modeltranslation.translator import register, TranslationOptions

from .models import FoodCategory, Vendor, VendorBranch


@register(FoodCategory)
class FoodCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Vendor)
class VendorTranslationOptions(TranslationOptions):
    fields = ('business_name', 'description', 'address')


@register(VendorBranch)
class VendorBranchTranslationOptions(TranslationOptions):
    fields = ('branch_name', 'short_description', 'address')







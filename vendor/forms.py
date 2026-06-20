from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# # import bleach

from .models import FoodCategory, VendorBranch


# HeroSlider Form 
class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ['is_active', 'order', 'name_en', 'name_ar', ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'



# Vendor Form 
# class VendorForm(forms.ModelForm):
#     class Meta:
#         model = Vendor
#         fields = ['is_active', 'order', 'logo', 'cover_photo', 'trade_license', 'is_approved', 'user',

#             # English fields
#             'business_name_en',
#             'description_en',
#             'address_en',

#             #Arabic fields
#             'business_name_ar',
#             'description_ar',
#             'address_ar',
#         ]
        
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save'))
#         # self.fields['category'].empty_label = 'Select Category'



# VendorBranch Form 
class VendorBranchForm(forms.ModelForm):
    class Meta:
        model = VendorBranch
        fields = ['is_active', 'order', 'thumbnail', 'categories',  'is_open',
                  
            #   'vendor',

            # English fields
            'branch_name_en',
            'short_description_en',
            'address_en',

            #Arabic fields
            'branch_name_ar',
            'short_description_ar',
            'address_ar',
        ]
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'


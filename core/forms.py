from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# # import bleach

from .models import HeroSlider, Partner, LeadershipMessage, WhyChooseUs, FAQ, SiteSetting
# from .models import Newsletter, Banner, 


# HeroSlider Form 
class HeroSliderForm(forms.ModelForm):
    class Meta:
        model = HeroSlider
        fields = ['is_active', 'order', 'image', 'primary_btn_url', 'secondary_btn_url',

            # English fields
            'heading_en',
            'short_description_en',
            'cta_message_en',
            'primary_btn_txt_en',
            'secondary_btn_txt_en',

            #Arabic fields
            'heading_ar',
            'short_description_ar',
            'cta_message_ar',
            'primary_btn_txt_ar',
            'secondary_btn_txt_ar',

        ]
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'



# Partner Form
class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))




# LeadershipMessage Form 
class LeadershipMessageForm(forms.ModelForm):
    class Meta:
        model = LeadershipMessage
        fields = ['is_active', 'order', 'photo',

            # English fields
            'heading_en',
            'name_en',
            'designation_en',
            'message_01_en',
            'message_02_en',

            # Arabic fields
            'heading_ar',
            'name_ar',
            'designation_ar',
            'message_01_ar',
            'message_02_ar',
        ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))



# WhyChooseUs Form 
class WhyChooseUsForm(forms.ModelForm):
    class Meta:
        model = WhyChooseUs
        fields = [
            'icon',
            'is_active',
            'order',

            # English fields
            'title_en',
            'description_en',

            # Arabic fields
            'title_ar',
            'description_ar',
        ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))



class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['is_active', 'order', 'question_en', 'answer_en', 'question_ar', 'answer_ar', 'faq_type',]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))




# SiteSetting Form 
class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = ['favicon', 'header_logo', 'footer_logo', 'email_sale', 'email_support', 
        
            'facebook_url', 
            'linkedin_url', 
            'instagram_url', 
            'youtube_url', 
            'tiktok_url', 

            'meta_title', 
            'meta_description', 
            'meta_keywords', 
            'og_image', 
            'google_site_verification', 

            # English fields
            'mobile_sale_en',
            'mobile_support_en',
            'address_en',
            'about_company_en',
            'office_hours_en',

            #Arabic fields
            'mobile_sale_ar',
            'mobile_support_ar',
            'address_ar',
            'about_company_ar',
            'office_hours_ar',
        ]
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'














# # Banner form 
# class BannerForm(forms.ModelForm):
#     class Meta:
#         model = Banner
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save'))


# # NewsletterForm
# class NewsletterForm(forms.ModelForm):
#     class Meta:
#         model = Newsletter
#         fields = '__all__'
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save'))
#         # self.fields['category'].empty_label = 'Select Category'
        


 






# # ///////////////////////

# # ContactForm 
# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['user_name', 'user_mobile', 'user_email', 'user_message']
        
#         widgets = {
#             'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name*'}),
#             'user_mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Mobile*'}),
#             'user_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
#             'user_message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Your Message*'}),
#         }



# class ContactStatusForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['remark', 'status']
        
#         widgets ={
#             'remark' : forms.Textarea(attrs={'class': 'form-control'}),
#             # 'status' : forms.ChoiceField(attrs={'class': 'form-control'}),
#         }
        


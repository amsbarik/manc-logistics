from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# # import bleach

from .models import HeroSlider, Partner, WhyChooseUs
# from .models import Newsletter, Banner, 



# HeroSlider Form 
class HeroSliderForm(forms.ModelForm):
    class Meta:
        model = HeroSlider
        fields = '__all__'
        
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
        


 
# class FAQForm(forms.ModelForm):
#     class Meta:
#         model = FAQ
#         fields = '__all__'
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save'))







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
        


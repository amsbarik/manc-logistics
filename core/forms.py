# from django import forms 
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
# # import bleach

# from .models import TopSlider, TopLink, Contact, FAQ
# from .models import Newsletter, Banner, Partner


# class TopSliderForm(forms.ModelForm):
#     class Meta:
#         model = TopSlider
#         fields = '__all__'
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save'))
#         # self.fields['category'].empty_label = 'Select Category'



from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# import bleach

from .models import TopSlider, TopLink, Contact, FAQ
from .models import Newsletter, Banner, Partner


class TopSliderForm(forms.ModelForm):
    class Meta:
        model = TopSlider
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'


# TopLink form 
class TopLinkForm(forms.ModelForm):
    class Meta:
        model = TopLink
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# Banner form 
class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# NewsletterForm
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'
        


 
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))



class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))





# ///////////////////////

# ContactForm 
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['user_name', 'user_mobile', 'user_email', 'user_message']
        
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name*'}),
            'user_mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Mobile*'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'user_message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Your Message*'}),
        }



class ContactStatusForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['remark', 'status']
        
        widgets ={
            'remark' : forms.Textarea(attrs={'class': 'form-control'}),
            # 'status' : forms.ChoiceField(attrs={'class': 'form-control'}),
        }
        
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.form_method = 'POST'
        #     self.helper.add_input(Submit('submit', 'Save'))
            
            
   


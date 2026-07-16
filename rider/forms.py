from django import forms
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



from accounts.models import RiderProfile

from .models import RiderRecruitment



# RiderRecruitment Form
class RiderRecruitmentForm(forms.ModelForm):

    class Meta:
        model = RiderRecruitment
        fields = ['is_active', 'thumbnail', 

            # english 
            'heading_en',
            'short_description_en',
            'with_car_txt_en',
            'without_car_txt_en',

            # arabic 
            'heading_ar',
            'short_description_ar',
            'with_car_txt_ar',
            'without_car_txt_ar',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))




# Rider update Form
class RiderForm(forms.ModelForm):
    class Meta:
        model = RiderProfile
        # fields = '__all__'
        exclude = ["user",]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))




# Rider status change Form
class RiderStatusForm(forms.ModelForm):
    class Meta:
        model = RiderProfile
        fields = ["status",]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update Status'))




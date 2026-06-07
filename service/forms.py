
from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# # import bleach

from .models import Service



# Service Form 
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['is_active', 'order', 'thumbnail', 'icon',

            # English fields
            'title_en',
            'short_description_en',
            
            #Arabic fields
            'short_description_ar',
            'title_ar',
            
        ]
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'


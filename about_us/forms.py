from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# # import bleach

from .models import WorkingProcess, ExpertTeam



# ExpertTeam Form 
class WorkingProcessForm(forms.ModelForm):
    class Meta:
        model = WorkingProcess
        fields = ['is_active', 'image',

            # English fields
            'title_en',
            'short_description_en',
            'order_en',

            #Arabic fields
            'title_ar',
            'short_description_ar',
            'order_ar',
        ]
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'


# //////////////////////////////////////////////////////////////////////////////////////      
# ExpertTeam Form 
class ExpertTeamForm(forms.ModelForm):
    class Meta:
        model = ExpertTeam
        fields = ['is_active', 'order', 'photo',

            # English fields
            'name_en',
            'designation_en',

            #Arabic fields
            'name_ar',
            'designation_ar',
        ]
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'

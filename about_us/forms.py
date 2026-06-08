from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import inlineformset_factory

from .models import About, WorkingProcess, ExpertTeam


# About Form
class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ['is_active', 'thumbnail', 
                  
                #   'mission_icon', 'vision_icon',

            # english 
            'heading_en',
            'short_description_en',
            'mission_en',
            'vision_en',
            'feature_01_en',
            'feature_02_en',
            'feature_03_en',
            'feature_04_en',
            'feature_05_en',
            'feature_06_en',
            'feature_07_en',

            # arabic 
            'heading_ar',
            'short_description_ar',
            'mission_ar',
            'vision_ar',
            'feature_01_ar',
            'feature_02_ar',
            'feature_03_ar',
            'feature_04_ar',
            'feature_05_ar',
            'feature_06_ar',
            'feature_07_ar',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


# /////////////////////////////////////////////

# ExpertTeam Form 
class WorkingProcessForm(forms.ModelForm):
    class Meta:
        model = WorkingProcess
        fields = ['is_active', 'image', 'order',

            # English fields
            'title_en',
            'short_description_en',

            #Arabic fields
            'title_ar',
            'short_description_ar',
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

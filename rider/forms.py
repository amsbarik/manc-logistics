from django import forms
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



from accounts.models import RiderProfile




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




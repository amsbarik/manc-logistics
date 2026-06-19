



from django import forms
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



from .models import RiderProfile


# admin login form
class CustomAdminLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label=''  # Hide label
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label=''  # Hide label
    )





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








# from django import forms
# from django.contrib.auth import get_user_model

# from .models import RiderProfile


# User = get_user_model()



# class RiderRegisterForm(forms.Form):

    # User
    full_name = forms.CharField(
        max_length=150
    )

    phone = forms.CharField(
        max_length=20
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )


    # Rider Profile

    nationality = forms.CharField(
        required=False
    )

    date_of_birth = forms.DateField(
        required=False
    )


    profile_photo = forms.ImageField(
        required=False
    )


    city = forms.CharField(
        max_length=100
    )


    address = forms.CharField(
        required=False,
        widget=forms.Textarea
    )


    iqama_number = forms.CharField(
        max_length=50
    )


    iqama_expired_date = forms.DateField(
        required=False
    )


    driving_license_number = forms.CharField(
        max_length=100
    )


    vehicle_type = forms.ChoiceField(
        choices=RiderProfile.VEHICLE_CHOICES
    )


    vehicle_plate_number = forms.CharField(
        required=False
    )


    iqama_image = forms.ImageField(
        required=False
    )


    license_image = forms.ImageField(
        required=False
    )


    def clean_phone(self):

        phone = self.cleaned_data["phone"]

        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError(
                "Phone already exists"
            )

        return phone



    def clean_iqama_number(self):

        iqama = self.cleaned_data["iqama_number"]

        if RiderProfile.objects.filter(
            iqama_number=iqama
        ).exists():

            raise forms.ValidationError(
                "Iqama already registered"
            )

        return iqama






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
        
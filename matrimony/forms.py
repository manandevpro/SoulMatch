from django import forms

from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

from .models import Profile, FatherProfile


# 1. Defining Cutom Validator
def my_email_validator(email):
    if email.split('@')[1].split('.')[0].lower() == "hotmail":
         raise ValidationError("Email not Acceptable")


class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    # email=forms.EmailField()
    # email=forms.CharField(validators=[EmailValidator()])
    email=forms.CharField(validators=[EmailValidator(), my_email_validator])  #Built-in & Custom validators Combined
    verify_email = forms.CharField()                                          #Defining custom 'cleaned data'  
    message=forms.CharField(widget=forms.Textarea)

    # 2. Custom Cleaning
    def clean(self):
        cleaned_data = super().clean()

        name= cleaned_data.get('name')
        cleaned_data['email']= cleaned_data.get('email').lower()
        cleaned_data['verify_email']= cleaned_data.get('verify_email').lower()
        message= cleaned_data.get('message')

        if cleaned_data.get('email') != cleaned_data.get('verify_email'):
            raise forms.ValidationError("Email Mismatched")
        
        return cleaned_data


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"
        # fields = ['name', 'age', 'gender']
        # exclude = ['is_married', 'name', 'age', 'profile_pic']
        

class FatherProfileForm(forms.ModelForm):

    class Meta:
        model = FatherProfile
        fields = "__all__"
        # fields = ['name', 'age', 'gender']
        # exclude = ['is_married', 'name', 'age', 'profile_pic']

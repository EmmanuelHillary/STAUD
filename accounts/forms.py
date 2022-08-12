from django import forms
from .models import BloggerProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accommodation.models import Campus
import re

CAMPUS = (('Campus', 'Campus'),)
for i in Campus.objects.all():
    CAMPUS += ((i.name, i.name),)

class BloggerJoin(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}))
    phone_number = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}))
    campus = forms.ChoiceField(choices=CAMPUS, widget=forms.Select(attrs={'class': 'form-loss', 'id': 'types'}))

    def clean_campus(self):
        campus = self.cleaned_data.get("campus")
        if campus == 'Campus':
            raise forms.ValidationError(
                "Select a campus"
            )

class BloggerEditProfile(forms.ModelForm):
    class Meta:
        model = BloggerProfile
        fields = ['name', 'email', 'phone_number', 'bio','display_picture']

class BloggerSignUp(UserCreationForm):
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2=forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
    
    def clean_password2(self):
        password = self.cleaned_data.get("password1")
        confirm_password = self.cleaned_data.get("password2")
        if password and confirm_password and  password != confirm_password:
            raise forms.ValidationError(
                "password and confirm password does not match."
            )
        if password and confirm_password and len(password) < 8:
            raise forms.ValidationError(
                "password must be at least 8 characters."
            )
        if password and confirm_password and not re.findall('\d', password):
            raise forms.ValidationError(
                "The password must contain at least 1 digit."
            )
        if password and confirm_password and not re.findall('[A-Z]', password):
            raise forms.ValidationError(
                "The password must contain at least 1 uppercase letter."
            )
        if password and confirm_password and not re.findall('[a-z]', password):
            raise forms.ValidationError(
                "The password must contain at least 1 lowercase letter."
            )
        return confirm_password
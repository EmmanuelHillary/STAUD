from django import forms
from .models import Subscribe, Newsletter
from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE

class SubscriptionForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}))
    class Meta:
        model = Subscribe
        fields = ['name', 'email']
    
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if Subscribe.objects.filter(email=email).exists():
                raise ValidationError('This email has already been used.')
            if email == "":
                raise ValidationError('Enter your email')
            return email

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if name == "":
                raise ValidationError('Enter your name')
            return name

class UnsubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['name', 'email']
    
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if not Subscribe.objects.filter(email=email).exists():
                return forms.ValidationError('This email does not exist.')
            return email

class NewsletterCreationForm(forms.ModelForm):

    email = forms.ModelMultipleChoiceField(queryset=Subscribe.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control col-8'}))

    class Meta:
        model = Newsletter
        fields = ['subject', 'body', 'email', 'status']

        widgets = {
           'subject': forms.TextInput(attrs={'class': 'form-control col-8'}),
           'status': forms.Select(attrs={'class': 'form-control col-8'}),
        }
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.widgets import Textarea

from site_setting.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'message']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'متن پیام'}),
        }

from django import forms 
from .models import TexttoHtml

class TexttoHtmlForm(forms.ModelForm):
    class Meta:
        model = TexttoHtml
        fields = ['text']    
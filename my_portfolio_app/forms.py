from django import forms
from .models import Contact

attrs = {"class":'input'}
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email','message']
        widgets = {
            'name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
            'message': forms.Textarea(attrs=attrs),
        }

    
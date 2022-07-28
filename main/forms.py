from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        name = Contact
        model = Contact
        fields = "__all__"
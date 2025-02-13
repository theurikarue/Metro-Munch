from django import forms
from .models import ContactMessage, Feedback

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class Feedback(forms.ModelForm):
    class Meta:  
        model = Feedback
        fields = ['names', 'email', 'message']

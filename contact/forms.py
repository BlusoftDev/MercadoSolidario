from django import forms
from .models import Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content', 'email']
    widgets = {
        'name': forms.TextInput(attrs={'class':'input  is-medium is-fullwidth mr-3','placeholder':'Nombre '}),
        'email': forms.TextInput(attrs={'class':' column is-4'}),
        'content': forms.Textarea(attrs={'class':' column is-4'}),
    }
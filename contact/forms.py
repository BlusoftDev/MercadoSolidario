from django import forms
from .models import Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre '}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Correo electrónico '}),
            'content': forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe tu comentario... '}),
        }
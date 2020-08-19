from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='' ,widget=forms.TextInput(attrs={'placeholder': 'Nombre','class':'input half-width ml-2 my-2 is-medium'}), required=True)
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email','class':'input half-width ml-2 my-2 is-medium', 'type':'email'}), required=True)
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Escribe tu comentario...','class':'textarea mt-3 mr-6 ml-2'}), required=True)
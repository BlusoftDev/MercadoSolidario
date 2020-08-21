from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'city', 'locality', 'postal_code', 'colony','street', 'ext_number', 'int_number','to_home', 'delivery_options',
        'platform', 'phone', 'cellphone', 'email', 'activity', 'subactivity', 'tags', 'payment_method', 'image','let_me_know_more','join', 'lat', 'long']
        widgets = {
            'locality': forms.Select(attrs={'id':'locality'}),
            'colony': forms.Select(attrs={'id':'colony'}),
            'postal_code': forms.TextInput(attrs={'id':'cp'}),
            'city': forms.Select(attrs={'id':'city'}),
            'postal_code': forms.TextInput(attrs={'class':'input column is-3 mx-3 is-medium', 'placeholder':'Código Postal*'}),
            'street': forms.TextInput(attrs={'class':'input  is-medium', 'placeholder':'Calle de tu local o donde pones tu negocio', 'id':'street'}),
            'ext_number' : forms.TextInput(attrs={'class':'input column is-6  mr-2 is-medium', 'placeholder':'Número Exterior', 'id' : 'extNumber'}),
            'int_number' : forms.TextInput(attrs={'class':'input column is-6 ml-2 is-medium', 'placeholder':'Número Interior', 'autocomplete' : 'off'}),
            'to_home' : forms.CheckboxInput(attrs={'type':'checkbox'}),
            'platform': forms.TextInput(attrs={'class':'input  is-medium mt-2', 'placeholder':'UberEats, DidiFood, Rappi, Pronto, Shopify, etc...'}),
            'phone' : forms.TextInput(attrs={'class':'input  is-medium mt-2', 'placeholder':'Número de télefono fijo de tu negocio'}),
            'cellphone' : forms.TextInput(attrs={'class':'input  is-medium mt-2', 'placeholder':'Número de télefono móvil de tu negocio*'}),
            'email' : forms.TextInput(attrs={'class':'input  is-medium mt-2', 'placeholder':'Correo Electrónico de tu negocio'}),
            'name' : forms.TextInput(attrs={'class':'input  is-medium mt-2', 'placeholder':'Nombre del negocio'}),
            'tags' : forms.TextInput(attrs={'class':'input  is-medium mt-2', 'placeholder':'Escribe 6 palabras clave que describan los productos o servicios que ofreces'}),
            'payment_method' : forms.CheckboxSelectMultiple(attrs={'class':'is-size-5  is-medium mt-2'}),
            'let_me_know_more' : forms.CheckboxInput(attrs={'class':'is-size-5  is-medium mt-2'}),
            'join':forms.CheckboxInput(attrs={'class':'is-size-5  is-medium mt-2'}),
            'lat' : forms.TextInput(attrs={'hidden':'true'}),
            'long':forms.TextInput(attrs={'hidden':'true'}),
            
        }


class CompanySearchForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['city', 'activity', ]



from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'city',  'postal_code', 'colony','street', 'ext_number', 'int_number','to_home', 'delivery_options',
        'platform', 'phone', 'cellphone', 'email', 'subactivity', 'tags', 'payment_method', 'image','let_me_know_more','join', 'lat', 'long','operation_start','registerSAT',
        'product1', 'product2', 'product3', 'product4', 'product5', 'product6']
        widgets = {
          
            'colony': forms.TextInput(attrs={'id':'colony' ,'class':'form-control','placeholder':'Colonia de tu local*'}),
            'postal_code': forms.TextInput(attrs={'id':'cp','class':'form-control'}),
            'city': forms.Select(attrs={'id':'city', 'class':'form-control'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código Postal*'}),
            'street': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Calle de tu local o donde pones tu negocio', 'id':'street'}),
            'ext_number' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número Exterior', 'id' : 'extNumber'}),
            'int_number' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número Interior', 'autocomplete' : 'off'}),
            'to_home' : forms.CheckboxInput(attrs={'type':'checkbox', 'class':'form-check-input checkbox-size'}),
            'delivery_options' : forms.Select(attrs={'class':'form-control'}),
            'platform': forms.TextInput(attrs={'class':'form-control', 'placeholder':'UberEats, DidiFood, Rappi, Pronto, Shopify, etc...'}),
            'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número de télefono fijo de tu negocio'}),
            'cellphone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número de télefono móvil de tu negocio*'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo Electrónico de tu negocio'}),
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del negocio*'}),
            'image' : forms.FileInput(attrs={'class' : 'imageInput'}),
            'product1' : forms.FileInput(attrs={'class' : 'imageInput'}),
            'product2' : forms.FileInput(attrs={'class' : 'imageInput'}),
            'product3' : forms.FileInput(attrs={'class' : 'imageInput'}),
            'product4' : forms.FileInput(attrs={'class' : 'imageInput'}),
            'product5' : forms.FileInput(attrs={'class' : 'imageInput'}),
            'product6' : forms.FileInput(attrs={'class' : 'imageInput'}),
            'tags' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe 6 palabras clave que describan los productos o servicios que ofreces'}),
            'payment_method' : forms.CheckboxSelectMultiple(attrs={}),
            'let_me_know_more' : forms.CheckboxInput(attrs={'type': 'checkbox', 'class':'form-check-input checkbox-size'}),
            'join':forms.CheckboxInput(attrs={'type': 'checkbox', 'class':'form-check-input checkbox-size'}),
            'registerSAT' : forms.CheckboxInput(attrs={'type':'checkbox', 'class':'form-check-input'}),
            'lat' : forms.TextInput(attrs={'hidden':'true'}),
            'long':forms.TextInput(attrs={'hidden':'true'}),
            'operation_start': forms.DateInput(
                format='%d/%m/%Y', 
                attrs={'class': 'form-control', 
                       'autocomplete': 'off',
                       'type':"date"}
                       
            ),
            'subactivity' : forms.Select(attrs={'class':'form-control'}),
        }


class CompanySearchForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['city', 'subactivity', ]




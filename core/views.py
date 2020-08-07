from django.shortcuts import render, HttpResponse

# Create your views here.
"""
Inicio / home
Buscador / search
Registro / register
Lista de negocios / businesses
Detalles de negocios / business
Blog / blog
Post /post
Contacto /contact
"""


def home(request):
    return render(request, "core/home.html")


def search(request):
    return render(request, "core/search.html")


def register(request):
    return HttpResponse('Registro')


def businesses(request):
    return HttpResponse('Negocios')


def business(request):
    return HttpResponse('Negocio')


def blog(request):
    return HttpResponse('Blog')


def post(request):
    return HttpResponse('Post')


def contact(request):
    return HttpResponse('Contacto')

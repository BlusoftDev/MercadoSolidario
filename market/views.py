from django.shortcuts import render
from .forms import CompanyForm, CompanySearchForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from .models import Company, City
from taggit.models import Tag
import csv
from django.http import HttpResponse

# Create your views here.
def search(request):
    companies = Company.objects.all()
    return render(request, "market/search.html", {'companies':companies})


def company_list(request):
    companies = Company.objects.all()
    tags = Tag.objects.all()
    cities = City.objects.all()
    return render(request, "market/company_list.html", {'companies':companies, 'tags':tags, 'cities':cities})



class CompanyCreate(CreateView):
    model = Company
    form_class = CompanyForm
    
    def get_success_url(self):
            return reverse('register')

class CompanyDetailView(DetailView):
    model = Company

def companyDB(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="companies.csv"'

    companies = Company.objects.all()

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Municipio', 'Localidad', 'CP', 'Colonia', 'Numero exterior', 'Numero interior', 'Servicio a domicilio', 'Entrega en', 'url plataforma', 'Telefono fijo', 'Telefono movil', 'Email', 'Actividad',  'Actividad especifica', 'Etiquetas',  'Metodos de pago', 'Desea contarnos mas..', 'Quiere ser parte del Mercado solidario'])
    for company in companies:
        if company.to_home:
                delivery ='si'
        else:
            delivery ='no'
        
        pTags = ''

        for tag in company.tags.all():
            pTags += tag.name+', '

        paymentOptions=''

        for payment in company.payment_method.all():
            paymentOptions += payment.name+', '

        if company.let_me_know_more:
                knowMore ='si'
        else:
            knowMore ='no'

        if company.join:
            wantJoin ='si'
        else:
            wantJoin ='no'
            
        writer.writerow([
            company.name, 
            company.city,
            company.locality,
            company.postal_code,
            company.colony,
            company.ext_number,
            company.int_number,
            delivery,
            company.delivery_options,
            company.platform,
            company.phone,
            company.cellphone,
            company.email,
            company.activity,
            company.subactivity,
            pTags,
            paymentOptions,
            knowMore,
            wantJoin
            ])
    

    return response

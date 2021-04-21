from django.shortcuts import render, HttpResponse
from market.models import Company
from .models import Banner

# Create your views here.
def home(request):
    companies = Company.objects.all()
    banner = Banner.objects.all().first()
    return render(request, "core/home.html", {'companies':companies, 'banner':banner})




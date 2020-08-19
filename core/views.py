from django.shortcuts import render, HttpResponse
from market.models import Company

# Create your views here.




def home(request):
    companies = Company.objects.all()
    return render(request, "core/home.html", {'companies':companies})



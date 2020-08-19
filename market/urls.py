from django.urls import path
from . import views
from .views import CompanyCreate, CompanyDetailView

urlpatterns = [
    path('', views.search, name='search'), 
    path('download/company/database/data', views.companyDB, name='data'), 
    path('company_list/', views.company_list, name='company_list'), 
    path('register/', CompanyCreate.as_view(), name='register'),
    path('company_list/company/<int:pk>', CompanyDetailView.as_view(), name='detail'),
]
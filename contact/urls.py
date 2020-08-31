from django.urls import path
from . import views
from .views import ContactCreate

urlpatterns = [
    # Paths del core
    
    path('', ContactCreate.as_view(), name='contact'),
]

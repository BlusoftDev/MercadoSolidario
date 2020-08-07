from django.urls import path
from . import views

urlpatterns = [
    # Paths del core
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('businesses/', views.businesses, name='businesses'),
    path('business', views.business, name='business'),
    path('blog', views.blog, name='blog'),
    path('post', views.post, name='post'),
    path('contact', views.contact, name='contact'),
]

from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from .models import Bussiness, Comment
from django.views.generic.edit import CreateView


# Create your views here.
# def contact(request):
#     contact_form = ContactForm()
#     if request.method =="POST":
#             contact_form = ContactForm(data = request.POST)
#             if contact_form.is_valid():
#                 name = request.POST.get('name','')
#                 email = request.POST.get('email','')
#                 content = request.POST.get('content','')
#                 #redirect
#                 return redirect(reverse('contact')+'?ok')
#     return render(request, "contact/contact.html",{'form':contact_form})


class ContactCreate(CreateView):
    model = Comment
    form_class = ContactForm

    def get_success_url(self):
            return reverse('home')
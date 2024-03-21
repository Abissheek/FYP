from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .forms import ContactForm
from .models import Contact


class ContactView(SuccessMessageMixin,CreateView):
    model=Contact
    form_class=ContactForm
    template_name="pages/contact.html"
    success_url='/'
    success_message="Your message was sent successfully"







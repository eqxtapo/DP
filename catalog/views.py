from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product

class HomeView(ListView):
    model = Product


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"



class ProductDetailView(DetailView):
    model = Product

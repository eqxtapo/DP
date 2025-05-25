from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/product_list.html', context)

def contacts(requests):
    return render(requests, 'catalog/contacts.html')

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_details.html", context)

from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(requests):
    return render(requests, 'catalog/contacts.html')

from django.shortcuts import render

def home(request):
    return render(request, 'templates/home.html')

def contacts(requests):
    return render(requests, 'templates/contacts.html')

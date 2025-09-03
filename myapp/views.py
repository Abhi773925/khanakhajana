from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'hero.html')

def hero(request):
    return render(request, 'hero.html')

def menu(request):
    return render(request,'menu.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
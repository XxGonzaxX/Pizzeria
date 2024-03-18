from django.shortcuts import render
from AppPizzeria.models import *


def bienvenida(request):
    return render(request, 'AppPizzeria/home.html')

def menu(request):
    return render(request, 'menu.html')

def login(request):
    return render(request, 'login.html')

def contacto(request):
    return render(request, 'contacto.html')


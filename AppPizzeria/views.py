from django.shortcuts import render
from django.http import HttpResponse
from AppPizzeria.models import *

from django.shortcuts import render

def bienvenida(request):
    return render(request, 'bienvenida.html')

def menu(request):
    return render(request, 'menu.html')

def login(request):
    return render(request, 'login.html')

def contacto(request):
    return render(request, 'contacto.html')


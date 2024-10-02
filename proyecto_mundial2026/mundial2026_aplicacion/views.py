
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def calendario (request):
    return render(request, 'calendario.html')

def equipos(request):
    return render(request, 'equipos.html')

def jugadores(request):

    return render(request, 'jugadores.html')

def login (request):
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfil.html')

def registro(request):
    return render(request, 'registro.html')

def tecnicos (request):
    return render(request, 'tecnicos.html')

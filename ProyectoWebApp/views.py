from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

def home(request):
    return render(request, 'ProyectoWebApp/home.html')

# def servicios viajo a urls.servicios!!!

def tienda(request):
    return render(request, 'ProyectoWebApp/tienda.html') 


# def blog viajo a urls.blog!!!  

    
def contacto(request):
    return render(request, 'ProyectoWebApp/contacto.html')


# Create your views here.

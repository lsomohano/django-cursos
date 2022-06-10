#from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.
def  busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["producto"]:
        #mensaje = "Articulo buscado: %r" %request.GET["producto"]
        producto = request.GET["producto"]
        if len(producto)>20:
            mensaje="Texto de búsqueda excede el tamaño permitido"
        else:    
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})
    else:
        mensaje = "No se a introducido ningun producto"
    
    return HttpResponse(mensaje)

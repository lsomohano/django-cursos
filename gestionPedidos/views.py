from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def  busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    mensaje = "Articulo buscado: %r" %request.GET["producto"]
    return HTTPResponse(mensaje)

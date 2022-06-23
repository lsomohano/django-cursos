#from http.client import HTTPResponse
import re
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

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

def contacto(request):
    if request.method == "POST":
        
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            send_mail(infForm['asunto'],infForm['mensaje'],infForm.get('email',''),['cursos@pildorasinformaticas.es'],)

            return render(request, "gracias.html")
        
        #asunto = request.POST["asunto"]
        #mensaje = request.POST["mensaje"]+ " " + request.POST["email"]
        #email_from = settings.EMAIL_HOST_USER
        #recipient_list=["lsomohano20@hotmail.com"]
        #send_mail(asunto,mensaje,email_from,recipient_list)

        #return render(request,"gracias.html")
        
    else:
        miFormulario=FormularioContacto()
    return render(request,"formulario_contacto.html",{"form":miFormulario})
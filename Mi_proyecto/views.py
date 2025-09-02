from django.shortcuts import render
from .models import Evento

# Create your views here.

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, "eventos/lista.html", {"eventos": eventos})

    
def buscar_eventos(request):
    query_nombre = request.GET.get("nombre", "")
    query_fecha = request.GET.get("fecha", "")
    query_lugar = request.GET.get("lugar", "")

    eventos = Evento.objects.all()

    if query_nombre:
        eventos = eventos.filter(nombre__icontains=query_nombre)
    if query_fecha:
        eventos = eventos.filter(fecha=query_fecha)
    if query_lugar:
        eventos = eventos.filter(lugar__icontains=query_lugar)

    return render(request, "eventos/buscar.html", {
        "eventos": eventos,
        "nombre": query_nombre,
        "fecha": query_fecha,
        "lugar": query_lugar,
    })
def inicio(request):
    return render(request, "inicio.html")

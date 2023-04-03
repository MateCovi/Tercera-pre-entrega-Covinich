from django.shortcuts import render
from django.http import HttpResponse

from hola_mundo.models import Tarea

# Create your views here.
def saludar(request):
    return HttpResponse("Hola Mundo!")

def mostrar_mis_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "AppCoder/index.html", {"tareas": tareas})

def agregar_una_tarea(request):
    nombre_tarea = request.GET.get("nombre")
    nueva_tarea = Tarea(nombre=nombre_tarea)
    nueva_tarea.save()
    return mostrar_mis_tareas(request)

def terminar_una_tarea(request, id):
    tarea = Tarea.objects.filter(id=id).first()
    tarea.terminar()
    tarea.save()
    return mostrar_mis_tareas(request)

def borrar_una_tarea(request, id):
    tarea = Tarea.objects.filter(id=id).first()
    tarea.delete()
    return mostrar_mis_tareas(request)

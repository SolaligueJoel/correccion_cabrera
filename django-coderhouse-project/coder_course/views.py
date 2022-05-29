import code
from django.shortcuts import render
from datetime import datetime
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from coder_course.forms import cargarFamilia, cargarRubro, cargarTarea
from coder_course.models import Familias, Insumos, Rubros, Tareas

# Create your views here.


def index2(request):
    return render(request, "coder_course/index.html")


def insumos(request):
    return render(request, "coder_course/insumos.html")

def tareas(request):
    if request.method == "POST":
        miFormulario = cargarTarea(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            tarea = Tareas(codigo=informacion["codigo"],rubro=informacion["rubro"],tarea=informacion["tarea"],unidad=informacion["unidad"],costo=informacion["costo"],fecha=informacion["fecha"],especificacion=informacion["especificacion"])
            tarea.save()

            
            return render (request,"coder_course/index.html")
                 
    else:
        miFormulario=cargarTarea()
    return render (request,"coder_course/tareas.html",{"miFormulario":miFormulario})

def rubros(request):
    if request.method == "POST":
        miFormulario = cargarRubro(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            rubro = Rubros(codigo=informacion["codigo"],nombre=informacion["nombre"])
            rubro.save()

            
            return render (request,"coder_course/index.html")
                 
    else:
        miFormulario=cargarRubro()
    return render (request,"coder_course/rubros.html",{"miFormulario":miFormulario})

#def familias(request):
    return render(request, "coder_course/familias.html" )

def iniciar(request):
    return render (request, "coder_course/iniciar.html")

def familias(request):
    if request.method == "POST":
        miFormulario = cargarFamilia(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            familia = Familias(codigo=informacion["codigo"],nombre=informacion["nombre"])
            familia.save()

            
            return render (request,"coder_course/index.html")
                 
    else:
        miFormulario=cargarFamilia()
    return render (request,"coder_course/familias.html",{"miFormulario":miFormulario})

def busquedaCodigo(request):
    return render(request, "coder_course/busquedaCodigo.html")

def buscar(request):
    if request.GET["codigo"]:
        codigo = request.GET['codigo']
        familia = Familias.objects.filter(codigo__icontains=codigo)
        return render(request,"coder_course/resultadosBusqueda.html", {"codigo":codigo, "familia":familia})
    else:
        respuesta = "No enviaste datos"
    return render(request, "coder_course/index.html",{"respuesta":respuesta})


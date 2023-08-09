from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import *
from .forms import *

# Create your views here.

def probandoTemplate(self):

    miHtml = open("C:/Users/maria/OneDrive/Escritorio/54185/proyecto/app1/templates/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

def curso_list(request):
    curso = Curso.objects.all()
    return render(request, 'curso_list.html', {'curso': curso})

def curso_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_comision = request.POST.get('numero_comision')
        curso = Curso(nombre=nombre, numero_comision=numero_comision)
        curso.save()
        return redirect('curso_list.html')

    return render(request, 'curso_create.html')

def index(request):
    return render(request, 'index.html')

def lista_entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'entregable_list.html', {'entregables': entregables})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor_list.html', {'profesores': profesores})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante_list.html', {'estudiantes': estudiantes})

def crear_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:index')  
    else:
        form = EntregableForm()
    return render(request, 'entregable_form.html', {'form': form})

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:index')  
    else:
        form = ProfesorForm()
    return render(request, 'profesor_form.html', {'form': form})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:index')  
    else:
        form = EstudianteForm()
    return render(request, 'estudiante_form.html', {'form': form})

def buscar_cursos_por_nombre(request):
    cursos = []
    form = CursoSearchForm(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if nombre:
            cursos = Curso.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscar_cursos.html', {'form': form, 'cursos': cursos})
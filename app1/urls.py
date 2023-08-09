from django.urls import path
from . import views

urlpatterns = [
    path('probandoTemplates/', views.probandoTemplate, name='probandoTemplates'),
    path('curso_list/', views.curso_list, name='curso_list'),
    path('curso_create/', views.curso_create, name='curso_create'),
    path('index/', views.index, name='index'),
    path('entregables/', views.lista_entregables, name='lista_entregables'),
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('alumnos/', views.lista_estudiantes, name='lista_alumnos'),
    path('entregable/create/', views.crear_entregable, name='entregable-create'),
    path('profesor/create/', views.crear_profesor, name='profesor-create'),
    path('estudiante/create/', views.crear_estudiante, name='estudiante-create'),
    path('buscar-por-nombre/', views.buscar_cursos_por_nombre, name='buscar_cursos_por_nombre'),
]


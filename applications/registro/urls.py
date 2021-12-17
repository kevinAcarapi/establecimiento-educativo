from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'registro_app'

urlpatterns = [
    path(
        "lista-docentes/", 
        views.EmpleadoDocenteListView.as_view(), 
        name="lista-docentes"
        ),
    path(
        "lista-no-docentes/", 
        views.EmpleadoNoDocenteListView.as_view(), 
        name="lista-no-docentes"
        ),
    path(
        "detalle-docente/<pk>/", 
        views.EmpleadoDocenteDetailView.as_view(), 
        name="detalle-docente"
        ),
    path(
        "detalle-no-docente/<pk>/", 
        views.EmpleadoNoDocenteDetailView.as_view(), 
        name="detalle-no-docente"
        ),
    path(
        "alta-docente/", 
        views.EmpleadoDocenteCreateView.as_view(), 
        name="alta-docente"
        ),
    path(
        "alta-no-docente/", 
        views.EmpleadoNoDocenteCreateView.as_view(), 
        name="alta-no-docente"
        ),
    path(
        "actualizar-docente/<pk>", 
        views.EmpleadoDocenteUpdateView.as_view(), 
        name="actualizar-docente"
        ),
    path(
        "actualizar-no-docente/<pk>", 
        views.EmpleadoNoDocenteUpdateView.as_view(), 
        name="actualizar-no-docente"
        ),
    path(
        "eliminar-docente/<pk>", 
        views.EmpleadoDocenteDeleteView.as_view(), 
        name="eliminar-docente"
        ),
    path(
        "eliminar-no-docente/<pk>", 
        views.EmpleadoNoDocenteDeleteView.as_view(), 
        name="eliminar-no-docente"
        ),
    path(
        "lista-materias/", 
        views.EmpleadoDocenteMateriaListView.as_view(), 
        name="lista-materias"
        ),
    path(
        "lista-oficinas/", 
        views.EmpleadoDocenteOficinaListView.as_view(), 
        name="lista-oficinas"
        ),
    path(
        "", 
        views.VistaPrincipal.as_view(), 
        name="index"
        ),
]

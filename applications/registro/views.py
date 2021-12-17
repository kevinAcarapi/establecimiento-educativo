from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy

from applications.registro.forms import EmpleadoDocenteForm, EmpleadoNoDocenteForm
from .models import EmpleadoDocente, EmpleadoNoDocente
from . forms import EmpleadoDocenteForm, EmpleadoNoDocenteForm

# Create your views here.

#Me mostrara la lista de empleados docentes en una tabla de 4 en 4 elementos
class EmpleadoDocenteListView(ListView): 
    model = EmpleadoDocente # tengo las materias y los campos para llenar un nuevo docente.
    template_name = "registro/list_all_teacher.html"
    ordering = 'last_name'
    context_object_name = 'listaDocente'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = EmpleadoDocente.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista

#Me mostrará la lista de empleados no docentes en una tabla de 4 en 4 elementos
class EmpleadoNoDocenteListView(ListView): 
    model = EmpleadoNoDocente # tengo las oficinas y los campos para llenar un nuevo no docente.
    template_name = "registro/list_all_Noteacher.html"
    ordering = 'last_name'
    context_object_name = 'listaNoDocente'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = EmpleadoNoDocente.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista

#Detalles de mis empleados docentes.
class EmpleadoDocenteDetailView(DetailView):
    model = EmpleadoDocente
    template_name = "registro/detail-teacher.html"
    context_object_name = 'detalleDocente'

#Detalles de mis empleados no docentes.
class EmpleadoNoDocenteDetailView(DetailView):
    model = EmpleadoNoDocente
    template_name = "registro/detail-no-teacher.html"
    context_object_name = 'detalleNoDocente'

#Dar de alta a un nuevo docente
class EmpleadoDocenteCreateView(CreateView):
    model = EmpleadoDocente
    template_name = "registro/high-teacher.html"
    form_class = EmpleadoDocenteForm

    success_url = reverse_lazy("registro_app:lista-docentes")

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoDocenteCreateView, self).form_valid(form)

#Dar de alta a un nuevo no docente.
class EmpleadoNoDocenteCreateView(CreateView):
    model = EmpleadoNoDocente
    template_name = "registro/high-no-teacher.html"
    form_class = EmpleadoNoDocenteForm

    success_url = reverse_lazy("registro_app:lista-no-docentes")

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoNoDocenteCreateView, self).form_valid(form)

#Modifcar datos de los empleados docentes que ya existan.
class EmpleadoDocenteUpdateView(UpdateView):
    model = EmpleadoDocente
    template_name = "registro/update-teacher.html"
    form_class = EmpleadoDocenteForm

    success_url = reverse_lazy("registro_app:lista-docentes")

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoDocenteUpdateView, self).form_valid(form)

#Modifcar datos de los empleados no docentes que ya existan.
class EmpleadoNoDocenteUpdateView(UpdateView):
    model = EmpleadoNoDocente
    template_name = "registro/update-no-teacher.html"
    form_class = EmpleadoNoDocenteForm

    success_url = reverse_lazy("registro_app:lista-no-docentes")

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoNoDocenteUpdateView, self).form_valid(form)

#Me elimina un empleado docente.
class EmpleadoDocenteDeleteView(DeleteView):
    model = EmpleadoDocente
    template_name = "registro/delete-teacher.html"

    success_url = reverse_lazy("registro_app:lista-docentes")

#Me elimina un empleado no docente.
class EmpleadoNoDocenteDeleteView(DeleteView):
    model = EmpleadoNoDocente
    template_name = "registro/delete-no-teacher.html"

    success_url = reverse_lazy("registro_app:lista-no-docentes")

#Me muestra la lista de materias.
class EmpleadoDocenteMateriaListView(ListView):
    model = EmpleadoDocente
    template_name = "registro/list-all-materias.html"
    context_object_name = 'materias'

    success_url = reverse_lazy("registro_app:lista-materias")

#Me muestra la lista de materias.
class EmpleadoDocenteOficinaListView(ListView):
    model = EmpleadoNoDocente
    template_name = "registro/list-all-offices.html"
    context_object_name = 'oficinas'

    success_url = reverse_lazy("registro_app:lista-oficinas")


#Mi index
class VistaPrincipal(TemplateView):
    template_name = 'index.html'


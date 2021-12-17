from django.contrib import admin
from .models import *

from applications.registro.models import DepartamentoDocente, EmpleadoDocente, Habilidad

# Register your models here.

"""       REGISTRO DE MIS MODELOS DOCENTES         """

admin.site.register(DepartamentoDocente)
admin.site.register(Habilidad)

class EmpleadoDocenteAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'departamento',
        'materia',
        'id',
    )

    search_fields = ('last_name', 'first_name')
    list_filter = ('materia', 'habilidad', 'departamento') #Filtrado lateral de la página.
    filter_horizontal = ('habilidad',) #Filtrado al agregar un nuevo docente / no docente en el campo habilidad.

admin.site.register(EmpleadoDocente, EmpleadoDocenteAdmin)

"""       REGISTRO DE MIS MODELOS NO DOCENTES         """

class EmpleadoNoDocenteAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'departamento',
        'oficina',
        'id',
    )

    search_fields = ('last_name', 'first_name',)
    list_filter = ('oficina', 'habilidad', 'departamento',) #Filtrado lateral de la página.
    filter_horizontal = ('habilidad',) #Filtrado al agregar un nuevo docente / no docente en el campo habilidad.

admin.site.register(EmpleadoNoDocente, EmpleadoNoDocenteAdmin)




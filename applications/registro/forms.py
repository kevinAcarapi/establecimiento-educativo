from django import forms
from django.forms.widgets import Widget
from .models import EmpleadoDocente, EmpleadoNoDocente

class EmpleadoDocenteForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""
        #Me crea campos para setar datos.
        model = EmpleadoDocente
        fields = (
        'last_name',
        'first_name',
        'materia',
        'departamento',
        'habilidad',
        'avatar'
        )
        #Me crea un checkbox con las opciones de mis habilidades.
        widgets = {
            'habilidad' : forms.CheckboxSelectMultiple() 
        }

class EmpleadoNoDocenteForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""
        #Me crea campos para setar datos.
        model = EmpleadoNoDocente
        fields = (
        'last_name',
        'first_name',
        'oficina',
        'departamento',
        'habilidad',
        'avatar'
        )
        #Me crea un checkbox con las opciones de mis habilidades.
        widgets = {
            'habilidad' : forms.CheckboxSelectMultiple() 
        }


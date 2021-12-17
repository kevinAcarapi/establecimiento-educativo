from django.db import models

# Create your models here.

"""               AREA DOCENTE                 """

class DepartamentoDocente(models.Model):
    #Me aparecen estos campos al querer agregar un departamento
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=50)

    #Nombres que se generan en mi administrador
    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        ordering = ['name']

    def __str__(self):
        return self.name

class Habilidad(models.Model):
    """Model definition for Habilidad."""

    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        """Meta definition for Habilidad."""

        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        """Unicode representation of Habilidad."""
        return self.habilidad



class EmpleadoDocente(models.Model):
    """Model definition for Docente."""

    MATERIA = (
        ('0','Sistemas Operativos'),
        ('1','Matemática Aplicada'),
        ('2','Modelado de Sistemas'),
        ('3','Programación II'),
        ('4','Base de Datos'),
        ('5','Practica Profesionalizante I'),
    )
    #Agregamos los campos para que llene el nuevo empleado.
    last_name = models.CharField('Nombre', max_length=50)
    first_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=50, blank=True)
    materia = models.CharField('Materia', max_length=50, choices=MATERIA)
    departamento = models.ForeignKey(DepartamentoDocente, on_delete=models.CASCADE) #Se utiliza para saber a que departamento pertence cada empleado. Como este atributo (campo) pertenece a otro modelo, se denomina ForeignKey.
    habilidad = models.ManyToManyField(Habilidad) #Habilidad que tendra mi docente/no docente. Campo denominado "muchos a muchos"
    avatar = models.ImageField('Imagen', upload_to='registro', height_field=None, width_field=None, max_length=None, blank=True)

    class Meta:
        """Meta definition for Docente."""

        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        """Unicode representation of Docente."""
        return self.last_name + ', ' + self.first_name


""" - - - - - - - - - - - - - - - - - - - - - - - - - - -"""


"""                 AREA NO DOCENTE                      """


class EmpleadoNoDocente(models.Model):
    """Model definition for Docente."""

    OFICINA = (
        ('0','Coordinación'),
        ('1','Limpieza'),
        ('2','Preceptoría'),
        ('3','Dirección'),
        ('4','Mantenimiento'),
        ('5','Otro'),
    )
    # Agregamos los campos para que llene un nuevo empleado
    last_name = models.CharField('Nombre', max_length=50)
    first_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=50, blank=True)
    oficina = models.CharField('Oficina', max_length=50, choices=OFICINA)
    departamento = models.ForeignKey(DepartamentoDocente, on_delete=models.CASCADE) #Se utiliza para saber a que departamento pertence cada empleado. Como este atributo (campo) pertenece a otro modelo, se denomina ForeignKey.
    habilidad = models.ManyToManyField(Habilidad) #Habilidad que tendra mi docente/no docente. Campo denominado "muchos a muchos"
    avatar = models.ImageField('Imagen', upload_to='registro', height_field=None, width_field=None, max_length=None, blank=True)

    class Meta:
        """Meta definition for Docente."""

        verbose_name = 'No Docente'
        verbose_name_plural = 'No Docentes'

    def __str__(self):
        """Unicode representation of Docente."""
        return self.last_name + ', ' + self.first_name




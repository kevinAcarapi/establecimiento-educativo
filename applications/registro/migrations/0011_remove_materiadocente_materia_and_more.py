# Generated by Django 4.0 on 2021-12-17 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0010_materia_oficina_oficinanodocente_materiadocente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materiadocente',
            name='materia',
        ),
        migrations.RemoveField(
            model_name='oficinanodocente',
            name='oficina',
        ),
        migrations.DeleteModel(
            name='Materia',
        ),
        migrations.DeleteModel(
            name='MateriaDocente',
        ),
        migrations.DeleteModel(
            name='Oficina',
        ),
        migrations.DeleteModel(
            name='OficinaNoDocente',
        ),
    ]

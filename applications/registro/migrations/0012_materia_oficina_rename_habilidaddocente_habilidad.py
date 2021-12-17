# Generated by Django 4.0 on 2021-12-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0011_remove_materiadocente_materia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=50, verbose_name='materia')),
            ],
            options={
                'verbose_name': 'materia',
                'verbose_name_plural': 'materias',
            },
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oficina', models.CharField(max_length=50, verbose_name='oficina')),
            ],
            options={
                'verbose_name': 'oficina',
                'verbose_name_plural': 'oficinas',
            },
        ),
        migrations.RenameModel(
            old_name='HabilidadDocente',
            new_name='Habilidad',
        ),
    ]

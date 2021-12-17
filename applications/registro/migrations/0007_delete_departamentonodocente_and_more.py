# Generated by Django 4.0 on 2021-12-16 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_alter_empleadonodocente_oficina'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DepartamentoNoDocente',
        ),
        migrations.DeleteModel(
            name='HabilidadNoDocente',
        ),
        migrations.AlterModelOptions(
            name='departamentodocente',
            options={'ordering': ['name'], 'verbose_name': 'Area', 'verbose_name_plural': 'Areas'},
        ),
        migrations.AlterModelOptions(
            name='habilidaddocente',
            options={'verbose_name': 'Habilidad', 'verbose_name_plural': 'Habilidades'},
        ),
    ]
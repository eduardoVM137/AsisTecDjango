# Generated by Django 5.0.4 on 2024-05-07 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maestro',
            old_name='apellido_materno',
            new_name='Apellido_Materno',
        ),
        migrations.RenameField(
            model_name='maestro',
            old_name='apellido_paterno',
            new_name='Apellido_Paterno',
        ),
        migrations.RenameField(
            model_name='maestro',
            old_name='nombre',
            new_name='Nombre',
        ),
        migrations.RenameField(
            model_name='maestro',
            old_name='idmaestro',
            new_name='idMaestro',
        ),
        migrations.AlterModelTable(
            name='maestro',
            table='maestro',
        ),
    ]

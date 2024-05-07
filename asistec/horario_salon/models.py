from django.db import models


class Horario_Salon(models.Model):
    idHorario = models.AutoField(primary_key=True)
    idMaestro = models.IntegerField()
    idMateria = models.IntegerField()
    idSalon = models.IntegerField()
    Numero_Alumnos = models.IntegerField()
    Fecha_Inicio = models.DateTimeField()
    Fecha_Fin = models.DateTimeField()

    class Meta:
        db_table = 'horario_salon'  # Nombre de la tabla en la base de datos
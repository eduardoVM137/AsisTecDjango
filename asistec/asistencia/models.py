from django.db import models 

class Asistencia(models.Model):
    idAsistencia = models.AutoField(primary_key=True)
    idHorario = models.IntegerField()#models.ForeignKey(Horario_Salon, on_delete=models.CASCADE)
    Hora_Entrada = models.DateTimeField()
    Hora_Salida = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'asistencia'  # Nombre de la tabla en la base de datos

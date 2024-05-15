from django.db import models

# Create your models here.
class Asistencia(models.Model):
    idMaestro = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Apellido_Paterno = models.CharField(max_length=255)
    Apellido_Materno = models.CharField(max_length=255)
    # ...otros campos como se necesiten

    class Meta:
        db_table = 'asistencia'  # Nombre de la tabla en la base de datos
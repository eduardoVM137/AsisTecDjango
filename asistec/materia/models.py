from django.db import models

# Create your models here.
class Materia(models.Model):
    idMateria = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255) 
    # ...otros campos como se necesiten

    class Meta:
        db_table = 'materia'  # Nombre de la tabla en la base de datos
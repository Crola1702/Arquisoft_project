from django.db import models

from estudiante.models import Estudiante
from universidad.models import Universidad

class HistorialAcademico(models.Model):
    carrera = models.CharField(max_length=50)
    pga = models.FloatField()
    numSemestresCursados = models.IntegerField()
    creditosAprobados = models.IntegerField()
    fechaIngreso = models.DateField()
    creditosActuales = models.IntegerField()
    status = models.BooleanField(default=True)
    
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, default=None)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return '{}'.format(self.estudiante)


from django.db import models
from estudiante.models import Estudiante
from mentor.models import Mentor
from manejadorDeCitas.models import Cita

# Create your models here.

class Reporte(models.Model):
    id_reporte = models.PositiveBigIntegerField(primary_key=True)
    num_citas_agendadas = models.IntegerField(default=0)
    num_citas_canceladas = models.IntegerField(default=0)
    num_citas_asistidas = models.IntegerField(default=0)
    informe = models.CharField(max_length=340, default="")
    nivel_satisfaccion = models.IntegerField(default=0)

    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, to_field='numeroDocumento')
    mentor = models.ManyToManyField(Mentor, blank=True)
    
    #citas = models.OneToOneField(Cita, on_delete=models.CASCADE, to_field='id')

    def __str__(self) -> str:
        return '{} : {}'.format(self.id_reporte, self.informe)

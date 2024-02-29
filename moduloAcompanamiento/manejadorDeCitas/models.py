from django.db import models
from mentor.models import Mentor
from estudiante.models import Estudiante
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Cita(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.CharField(max_length=200)
    asistido = models.BooleanField(default=None, null=True)
    calificacion = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, to_field='numeroDocumento')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, to_field='numeroDocumento')

    class Meta:
        ordering = ["fecha"]

    def __str__(self):
        return f"{self.fecha} {self.hora} : ({self.estudiante} | {self.mentor})"
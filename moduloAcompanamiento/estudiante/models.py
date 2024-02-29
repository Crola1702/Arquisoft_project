from django.db import models


class Estudiante(models.Model):
    class Meta:
        ordering = ['numeroDocumento']

    TIPO_DOCUMENTO = [
            ("CC", "CC"),
            ("TI", "TI"),
            ("NIT", "NIT"),
    ]

    ESTADO_CIVIL = [
            ("Soltero", "Soltero"),
            ("Casado", "Casado"),
            ("Divorciado", "Divorciado"),
    ]

    nombre = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    correo = models.EmailField()
    tipoDocumento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO)
    numeroDocumento = models.PositiveBigIntegerField(primary_key=True)
    numeroTelefonico = models.PositiveBigIntegerField()
    ciudadania = models.CharField(max_length=50)
    estadoCivil = models.CharField(max_length=20, choices=ESTADO_CIVIL)
    carrera = models.CharField(max_length=50)
    semestre = models.IntegerField()

    def __str__(self) -> str:
        return '{} : {}'.format(self.numeroDocumento, self.nombre)

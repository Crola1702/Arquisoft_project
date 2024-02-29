from django.db import models
# Create your models here.

class Universidad(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    lugar = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

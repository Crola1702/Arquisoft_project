from ..models import Estudiante
from reporte.logic import logic_reportes

def getEstudiantes():
    estudiantes = Estudiante.objects.all()
    return estudiantes


def getEstudiante(id):
    estudiante = Estudiante.objects.get(numeroDocumento=id)
    return estudiante


def createEstudiante(est):
    estudiante = Estudiante(est["nombre"], est["fechaNacimiento"], est["correo"], est["tipoDocumento"], est["numeroDocumento"],
                            est["numeroTelefonico"], est["ciudadania"], est["estadoCivil"], est["carrera"], est["semestre"])
    estudiante.save()
    logic_reportes.create_empty_reporte(estudiante.numeroDocumento)
    return getEstudiante(estudiante.numeroDocumento)


def updateEstudiante(est_pk, est):
    estudiante = getEstudiante(est_pk)
    estudiante.nombre = est["nombre"]
    estudiante.fechaNacimiento = est["fechaNacimiento"]
    estudiante.correo = est["correo"]
    estudiante.tipoDocumento = est["tipoDocumento"]
    estudiante.numeroDocumento = est["numeroDocumento"]
    estudiante.numeroTelefonico = est["numeroTelefonico"]
    estudiante.ciudadania = est["ciudadania"]
    estudiante.estadoCivil = est["estadoCivil"]
    estudiante.carrera = est["carrera"]
    estudiante.semestre = est["semestre"]
    estudiante.save()
    return getEstudiante(estudiante.numeroDocumento)


def deleteEstudiante(est_pk):
    estudiante = getEstudiante(est_pk)
    estudiante.delete()
    return estudiante

from manejadorDeCitas.models import Cita
from reporte.logic import logic_reportes
from mentor.logic import logic_mentores

def getCitas():
    citas = Cita.objects.all()
    return citas


def getCita(id):
    cita = Cita.objects.get(id=id)
    return cita


def createCita(cita):
    cita = Cita(None, cita["fecha"], cita["hora"], cita["descripcion"], cita["asistido"], cita["calificacion"], cita["estudiante"], cita["mentor"])
    cita.save()
    logic_reportes.update_reporte_nueva_cita(cita.estudiante.numeroDocumento, cita)
    return getCita(cita.id)


def updateCita(cita_pk, cita_data):
    cita = getCita(cita_pk)
    cita.fecha = cita_data["fecha"]
    cita.hora = cita_data["hora"]
    cita.descripcion = cita_data["descripcion"]
    cita.asistido = cita_data["asistido"]
    cita.calificacion = cita_data["calificacion"]
    cita.save()
    logic_reportes.update_reporte_update_cita(cita.estudiante.numeroDocumento, cita)
    return getCita(cita_pk)


def deleteCita(cita_pk):
    cita = getCita(cita_pk)
    cita.delete()
    return cita
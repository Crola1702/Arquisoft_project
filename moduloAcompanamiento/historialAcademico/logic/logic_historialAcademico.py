from ..models import HistorialAcademico
from estudiante.logic import logic_estudiantes
from universidad.logic import logic_universidades

def get_historialesAcademicos():
    historialesAcademicos = HistorialAcademico.objects.all()
    return historialesAcademicos

def get_historialAcademico(his_pk):
    historialAcademico = HistorialAcademico.objects.get(pk=his_pk)
    return historialAcademico

def update_historialAcademico(his_pk, new_his):
    historialAcademico = get_historialAcademico(his_pk)
    historialAcademico.carrera = new_his["carrera"]
    historialAcademico.pga = new_his["pga"]
    historialAcademico.numSemestresCursados = new_his["numSemestresCursado"]
    historialAcademico.creditosAprobados = new_his["creditosAprobados"]
    historialAcademico.fechaIngreso = new_his["fechaIngreso"]
    historialAcademico.creditosActuales = new_his["fechaIngreso"]
    historialAcademico.status = new_his["status"]
    historialAcademico.save()
    return historialAcademico

def create_historialAcademico(his):

    estudianteOb = logic_estudiantes.getEstudiante(his["estudiante"])
    universidadOb = logic_universidades.getUniversidad(his["universidad"])

    historialAcademico = HistorialAcademico(
        carrera = his["carrera"],
        pga = his["pga"],
        numSemestresCursados = his["numSemestresCursados"],
        creditosAprobados = his["numSemestresCursados"],
        fechaIngreso = his["fechaIngreso"],
        creditosActuales = his["creditosActuales"],
        status = his["status"],
        estudiante = estudianteOb,
        universidad = universidadOb
    )
    historialAcademico.save()
    return get_historialAcademico(historialAcademico.pk)

def delete_historialAcademico(his_pk):
    historialAcademico = get_historialAcademico(his_pk)
    historialAcademico.delete()
    return historialAcademico 





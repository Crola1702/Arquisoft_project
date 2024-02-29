from ..models import Reporte
from estudiante.logic import logic_estudiantes
from mentor.logic import logic_mentores

def get_reportes():
    reportes = Reporte.objects.all()
    return reportes

def get_reporte(rep_pk):
    reporte = Reporte.objects.get(pk=rep_pk)
    return reporte

def get_reporte_by_estudiante(estudiante_pk):
    estudiante = logic_estudiantes.getEstudiante(estudiante_pk)
    reportes = Reporte.objects.filter(estudiante=estudiante)
    return reportes

def update_reporte_nueva_cita(rep_pk, cita):
    reporte = get_reporte(rep_pk)
    if reporte.num_citas_agendadas == 0:
        reporte.nivel_satisfaccion = cita.calificacion
    else:
        reporte.nivel_satisfaccion = (reporte.nivel_satisfaccion*reporte.num_citas_agendadas + cita.calificacion)/(reporte.num_citas_agendadas+1)
    
    reporte.num_citas_agendadas += 1
    if cita.asistido is not None:
        if cita.asistido:
            reporte.num_citas_asistidas += 1
        else:
            reporte.num_citas_canceladas += 1
    reporte.informe += f"{cita.fecha} - {cita.descripcion};"
    reporte.mentor.add(cita.mentor)
    reporte.save()

def update_reporte_update_cita(rep_pk, cita):
    # TODO
    reporte = get_reporte(rep_pk)
    if cita.asistido is not None:
        if cita.asistido:
            reporte.num_citas_asistidas += 1
        else:
            reporte.num_citas_canceladas += 1
    reporte.informe = f"{cita.fecha} - {cita.descripcion}"
    reporte.save()

def update_reporte(rep_pk, new_rep):
    reporte = get_reporte(rep_pk)
    reporte.num_citas_agendadas = new_rep["fields"]["num_citas_agendadas"]
    reporte.num_citas_canceladas = new_rep["fields"]["num_citas_canceladas"]
    reporte.num_citas_asistidas = new_rep["fields"]["num_citas_asistidas"]
    reporte.informe = new_rep["fields"]["informe"]
    reporte.nivel_satisfaccion = new_rep["fields"]["nivel_satisfaccion"]
    reporte.save()
    return reporte

def create_reporte(rep):
    estudiante = logic_estudiantes.getEstudiante(rep["fields"]["estudiante"])
    reporte = Reporte(num_citas_agendadas=rep["fields"]["num_citas_agendadas"], num_citas_canceladas=rep["fields"]["num_citas_canceladas"],
    num_citas_asistidas=rep["fields"]["num_citas_asistidas"], informe=rep["fields"]["informe"],
    nivel_satisfaccion=rep["fields"]["nivel_satisfaccion"], estudiante=estudiante, id_reporte=estudiante.numeroDocumento)
    mentores = rep["fields"]["mentor"]
    reporte.save()
    for mentor in mentores:
        reporte.mentor.add(mentor)
    return reporte

def create_empty_reporte(estudiante_pk):
    estudiante = logic_estudiantes.getEstudiante(estudiante_pk)
    reporte = Reporte(num_citas_agendadas=0, num_citas_canceladas=0, num_citas_asistidas=0, informe="",
    nivel_satisfaccion=0, estudiante=estudiante, id_reporte=estudiante.numeroDocumento)
    reporte.save()
    return reporte

def delete_reporte(reporte_pk):
    reporte = get_reporte(reporte_pk)
    reporte.delete()
    return reporte
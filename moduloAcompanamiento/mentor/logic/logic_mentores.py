from ..models import Mentor

def getMentores():
    mentores = Mentor.objects.all()
    return mentores

def getMentor(id):
    mentor = Mentor.objects.get(numeroDocumento=id)
    return mentor

def createMentor(data):
    mentor = Mentor(
        nombre = data['nombre'],
        fechaNacimiento = data['fechaNacimiento'],
        correo = data['correo'],
        tipoDocumento = data['tipoDocumento'],
        numeroDocumento = data['numeroDocumento'],
        numeroTelefonico = data['numeroTelefonico'],
        ciudadania = data['ciudadania'],
        estadoCivil = data['estadoCivil'],
        )
    mentor.save()
    return getMentor(mentor.numeroDocumento)

def updateMentor(pk, data):
    mentor = getMentor(pk)
    mentor.nombre = data['nombre']
    mentor.fechaNacimiento = data['fechaNacimiento']
    mentor.correo = data['correo']
    mentor.tipoDocumento = data['tipoDocumento']
    mentor.numeroTelefonico = data['numeroTelefonico']
    mentor.ciudadania = data['ciudadania']
    mentor.estadoCivil = data['estadoCivil']
    mentor.save()
    return getMentor(mentor.numeroDocumento)

def deleteMentor(pk):
    mentor = getMentor(pk)
    mentor.delete()
    return mentor
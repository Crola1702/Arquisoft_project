from ..models import Universidad


def getUniversidades():
    universidades = Universidad.objects.all()
    return universidades

def getUniversidad(u_pk):
    print(u_pk)
    u_pk = u_pk.replace("-", " ")
    universidad = Universidad.objects.get(pk=u_pk)
    return universidad


def updateUniversidad(u_pk, new_u):
    universidad = getUniversidad(u_pk)
    universidad.nombre = new_u["nombre"]
    universidad.lugar = new_u["lugar"]
    universidad.save()
    return universidad

def createUniversidad(u):
    universidad = Universidad(nombre=u["nombre"], lugar= u["lugar"] )
    universidad.save()
    return universidad
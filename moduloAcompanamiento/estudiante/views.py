from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic import logic_estudiantes
import json
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("Página principal de estudiantes")

@csrf_exempt
def estudiantes_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            estudiante_dto = logic_estudiantes.getEstudiante(id)
            estudiante = serializers.serialize('json', [estudiante_dto,])
            return HttpResponse(estudiante, 'application/json')
        else:
            estudiantes = logic_estudiantes.getEstudiantes()
            estudiantes_dto = serializers.serialize('json', estudiantes)
            return HttpResponse(estudiantes_dto, content_type='application/json')

    elif request.method == 'POST':
        estudiante = logic_estudiantes.createEstudiante(json.loads(request.body))
        if estudiante is None:
            return HttpResponse("Error al crear el estudiante", status=400)
        else:
            estudiante_dto = serializers.serialize('json', [estudiante,])
            return HttpResponse(estudiante_dto, content_type='application/json', status=201)

@csrf_exempt
def estudiante_view(request, pk):
    if request.method == 'GET':
        estudiante_dto = logic_estudiantes.getEstudiante(pk)
        estudiante = serializers.serialize('json', [estudiante_dto,])
        return HttpResponse(estudiante, 'application/json')

    elif request.method == 'PUT':
        estudiante = logic_estudiantes.updateEstudiante(pk, json.loads(request.body))
        estudiante_dto = serializers.serialize('json', [estudiante,])
        return HttpResponse(estudiante_dto, content_type='application/json', status=201)
    
    elif request.method == 'DELETE':
        estudiante = logic_estudiantes.deleteEstudiante(pk)
        estudiante_dto = serializers.serialize('json', [estudiante,])
        return HttpResponse(estudiante_dto, content_type='application/json', status=204)

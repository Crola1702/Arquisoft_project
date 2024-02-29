from django.shortcuts import render
from .logic import logic_historialAcademico as lha
from django.core import serializers
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt    
def historialesAcademicos_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            historialAcademico_dto = lha.get_historialAcademico(id)
            historialAcademico = serializers.serialize('json', [historialAcademico_dto,])
            return HttpResponse(historialAcademico, 'application/json')
        else:
            historialesAcademicos_dto = lha.get_historialesAcademicos()
            historialesAcademicos = serializers.serialize('json', historialesAcademicos_dto)
            return HttpResponse(historialesAcademicos, 'application/json')
    
    if request.method == 'POST':
        historialAcademico = lha.create_historialAcademico(json.loads(request.body))
        if historialAcademico is None:
            return HttpResponse("Error al crear el historial académico.", status=400)
        else:
            historialAcademico_dto = serializers.serialize('json', [historialAcademico,])
            return HttpResponse(historialAcademico_dto, content_type = 'application/json', status=201)

@csrf_exempt
def historialAcademico_view(request, pk):
    if request.method == 'GET':
        historialAcademico_dto = lha.get_historialAcademico(pk)
        historialAcademico = serializers.serialize('json', [historialAcademico_dto,])
        return HttpResponse(historialAcademico, 'application/json')
    
    elif request.method == 'PUT':
        historialAcademico = lha.update_historialAcademico(pk, json.loads(request.body))
        historialAcademico_dto = serializers.serialize('json', [historialAcademico,])
        return HttpResponse(historialAcademico_dto, content_type='application/json', status=201)
    
    elif request.method == 'DELETE':
        historialAcademico = lha.delete_historialAcademico(pk)
        historialAcademico_dto = serializers.serialize('json', [historialAcademico,])
        return HttpResponse(historialAcademico_dto, content_type='application/json', status=204)

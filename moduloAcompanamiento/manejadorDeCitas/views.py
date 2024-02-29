from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic import logic_citas
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return HttpResponse("Página principal de citas")


@csrf_exempt
def citas_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            cita_dto = logic_citas.getCita(id)
            cita = serializers.serialize('json', [cita_dto,])
            return HttpResponse(cita, 'application/json')
        else:
            citas = logic_citas.getCitas()
            citas_dto = serializers.serialize('json', citas)
            return HttpResponse(citas_dto, content_type='application/json')

    elif request.method == 'POST':
        cita = logic_citas.createCita(json.loads(request.body))
        if cita is None:
            return HttpResponse("Error al crear la cita", status=400)
        else:
            cita_dto = serializers.serialize('json', [cita,])
            return HttpResponse(cita_dto, content_type='application/json', status=201)

@csrf_exempt
def cita_view(request, pk):
    if request.method == 'GET':
        cita_dto = logic_citas.getCita(pk)
        cita = serializers.serialize('json', [cita_dto,])
        return HttpResponse(cita, 'application/json')

    elif request.method == 'PUT':
        cita = logic_citas.updateCita(pk, json.loads(request.body))
        cita_dto = serializers.serialize('json', [cita,])
        return HttpResponse(cita_dto, content_type='application/json', status=201)

    elif request.method == 'DELETE':
        cita = logic_citas.deleteCita(pk)
        cita_dto = serializers.serialize('json', [cita,])
        return HttpResponse(cita_dto, content_type='application/json', status=204)


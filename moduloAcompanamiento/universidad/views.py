import re
from django.shortcuts import render
from .logic import logic_universidades as lu
from django.core import serializers
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def universidades_view(request):
    if request.method == 'GET':
        nombre = request.GET.get("nombre", None)
        if nombre:
            universidad_dto = lu.getUniversidad(nombre)
            universidad = serializers.serialize('json', [universidad_dto,])
            return HttpResponse (universidad, 'application/json')
        else:
            universidad_dto = lu.getUniversidades()
            universidades = serializers.serialize('json', universidad_dto)
            return HttpResponse (universidades, 'application/json')
    elif request.method == 'POST':
        universidad = lu.createUniversidad(json.loads(request.body))
        if universidad is None:
            return HttpResponse("Error al crear la universidad", status=400)
        else:
            universidad_dto = serializers.serialize('json', [universidad,])
            return HttpResponse(universidad_dto, content_type='application/json', status=201)

@csrf_exempt
def universidad_view(request, pk):
    if request.method == 'GET':
        universidad_dto = lu.getUniversidad(pk)
        universidad= serializers.serialize('json', [universidad_dto,])
        return HttpResponse(universidad, 'application/json')

    if request.method == 'PUT':
        universidad_dto = lu.updateUniversidad(pk, json.loads(request.body))
        print(type(universidad_dto))
        universidad = serializers.serialize('json', [universidad_dto,])
        return HttpResponse(universidad, 'application/json')

# Create your views here.

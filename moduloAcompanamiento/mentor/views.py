from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic import logic_mentores
import json
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("Página principal de mentores")

@csrf_exempt
def mentores_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            mentor_dto = logic_mentores.getMentor(id)
            mentor = serializers.serialize('json', [mentor_dto,])
            return HttpResponse(mentor, 'application/json')
        else:
            mentores = logic_mentores.getMentores()
            mentores_dto = serializers.serialize('json', mentores)
            return HttpResponse(mentores_dto, content_type='application/json')

    elif request.method == 'POST':
        mentor = logic_mentores.createMentor(json.loads(request.body))
        if mentor is None:
            return HttpResponse("Error al crear el mentor", status=400)
        else:
            mentor_dto = serializers.serialize('json', [mentor,])
            return HttpResponse(mentor_dto, content_type='application/json', status=201)

@csrf_exempt
def mentor_view(request, pk):
    if request.method == 'GET':
        mentor_dto = logic_mentores.getMentor(pk)
        mentor = serializers.serialize('json', [mentor_dto,])
        return HttpResponse(mentor, 'application/json')

    elif request.method == 'PUT':
        mentor = logic_mentores.updateMentor(pk, json.loads(request.body))
        mentor_dto = serializers.serialize('json', [mentor,])
        return HttpResponse(mentor_dto, content_type='application/json', status=201)

    elif request.method == 'DELETE':
        mentor = logic_mentores.deleteMentor(pk)
        mentor_dto = serializers.serialize('json', [mentor,])
        return HttpResponse(mentor_dto, content_type='application/json', status=204)  

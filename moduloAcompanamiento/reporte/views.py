from os import stat
from django.shortcuts import render
from .logic import logic_reportes as rl
from django.core import serializers
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def reportes_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            reporte_dto = rl.get_reporte(id)
            reporte = serializers.serialize('json', [reporte_dto,])
            return HttpResponse(reporte, 'application/json', status = 200)
        else:
            reportes_dto = rl.get_reportes()
            reportes = serializers.serialize('json', reportes_dto)
            return HttpResponse(reportes, 'application/json', status = 200)

    if request.method == 'POST':
        reporte_dto = rl.create_reporte(json.loads(request.body))
        reporte = serializers.serialize('json', [reporte_dto,])
        return HttpResponse(reporte, 'application/json', status = 200)

@csrf_exempt
def reporte_view(request, pk):
    if request.method == 'GET':
        reporte_dto = rl.get_reporte(pk)
        reporte = serializers.serialize('json', [reporte_dto,])
        return HttpResponse(reporte, 'application/json', status = 200)

    if request.method == 'PUT':
        reporte_dto = rl.update_reporte(pk, json.loads(request.body))
        print(type(reporte_dto))
        reporte = serializers.serialize('json', [reporte_dto,])
        return HttpResponse(reporte, 'application/json', status = 200)
    
    elif request.method == 'DELETE':
        reporte = rl.delete_reporte(pk)
        reporte_dto = serializers.serialize('json', [reporte,])
        return HttpResponse(reporte_dto, content_type='application/json', status=200)
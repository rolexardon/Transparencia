from django import template
from Administration.models import CentroEducativo as CE
from datetime import datetime as dt

register = template.Library()

@register.filter(name='iteminlist')
def iteminlist(data,index):
    
    value = data[index]
    if value == "":
        value = 0
    return value
@register.filter(name='getinfocentro')
def getinfocentro(codigo,tipo):
    
    if codigo != None:
        if tipo == "nombre":
            value = CE.objects.get(pk=codigo.pk).nombre
        if tipo == "codigo":
            value = CE.objects.get(pk=codigo.pk).codigo_ce
        if tipo == "tipo":
            value = CE.objects.get(pk=codigo.pk).tipo_centro
    else:
        value=""
    
    return value    
    
    
@register.filter(name='getallcentros')
def getallcentros(codigo):
    
    if codigo != None:
        dep = CE.objects.get(pk=codigo.pk).codigo_departamento
        mun = CE.objects.get(pk=codigo.pk).codigo_municipio
    
        centros = CE.objects.filter(codigo_departamento = dep,codigo_municipio=mun).order_by('nombre')

        return centros
@register.filter(name='setval')
def setval(value,tipo):
    
    if value != None:
        if tipo == "fecha":
            return value
        if tipo == "tel":
            return value
    else:
        if tipo == "fecha":
            return dt.today()
        if tipo == "tel":
            return ""
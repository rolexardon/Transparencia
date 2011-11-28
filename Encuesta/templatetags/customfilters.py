from django import template
from Administration.models import CentroEducativo as CE

register = template.Library()

@register.filter(name='iteminlist')
def iteminlist(data,index):

    return data[index]
@register.filter(name='getinfocentro')
def getinfocentro(codigo,tipo):
    
    if tipo == "nombre":
        nombre = CE.objects.get(pk=codigo.pk).nombre
    
    return nombre
@register.filter(name='getallcentros')
def getallcentros(codigo):
    
    dep = CE.objects.get(pk=codigo.pk).codigo_departamento
    mun = CE.objects.get(pk=codigo.pk).codigo_municipio
    
    centros = CE.objects.filter(codigo_departamento = dep,codigo_municipio=mun).order_by('nombre').exclude(pk=codigo.pk)
    
    return centros
from django import template
from Administration.models import CentroEducativo as CE
from Administration.models import Departamento as D
from Administration.models import Municipio as M
from Encuesta.models import EncuestaData as ED

from datetime import datetime as dt

register = template.Library()

@register.filter(name='iteminlist')
def iteminlist(data,index):
    value = data[index]
    print value
    if value == "":
        value = ""
    if value == "0/":
        value = 0
    print value
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
   
@register.filter(name='getdepforcentro')    
def getdepforcentro(codigo):
    if codigo != None:
        dep = CE.objects.get(pk=codigo.pk).codigo_departamento
        depto = D.objects.get(codigo=dep).nombre
        return depto

@register.filter(name='getmunsforcentro')
def getmunsforcentro(codigo):
    if codigo != None:
        dep = CE.objects.get(pk=codigo.pk).codigo_departamento
        
        muns = M.FilterByDep(dep)
        return muns
    
@register.filter(name='getmunforcentro')
def getmunforcentro(codigo):
    if codigo != None:
        mun = CE.objects.get(pk=codigo.pk).codigo_municipio
        dep = CE.objects.get(pk=codigo.pk).codigo_departamento

        muni = M.objects.get(codigo=mun,departamento = dep).nombre

        return muni
    
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
        if tipo == "alumnos":
            return value
    else:
        if tipo == "fecha":
            return dt.today()
        if tipo == "tel":
            return ""
        if tipo == "alumnos":
            return ""
        
@register.filter(name='GetSpecificInfo')        
def GetSpecificInfo(encuesta):
    resultado = ""
    for x  in range(1,8):
        info = ED.BringValue(encuesta,'E',x)
        resultado += "E"+str(x)+ ": " + info + "    "
    return resultado

    
@register.filter(name='parsed_date')
def parsed_date(date):
    if date:
        today= date.strftime('%d/%m/%y')
    else:
        today="No ha seleccionado fecha"
    return today
   
   
@register.filter(name='centroinfo')
def centroinfo(centro):
    if centro:
        dep = D.objects.get(codigo=centro.codigo_departamento).nombre
        mun = M.objects.get(departamento = centro.codigo_departamento, codigo=centro.codigo_municipio).nombre
        
        ret = "[" + centro.codigo_ce + "] " + centro.nombre + ", " + mun + ", " + dep
    else:
        ret="No ha seleccionado centro"
    return ret
        
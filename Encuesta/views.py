from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.utils import simplejson

from Encuesta.models import SegmentoA as SA
from Encuesta.models import SegmentoB as SB
from Encuesta.models import SegmentoC as SC
from Encuesta.models import SegmentoD as SD
from Encuesta.models import SegmentoE as SE
from Encuesta.models import SegmentoF as SF
from Encuesta.models import SegmentoG as SG
from Encuesta.models import EncuestaTemp as ET
from Encuesta.models import EncuestaTempData as ETD

from Administration.models import CentroEducativo as CE
from Administration.models import Departamento as DP
from Administration.models import Municipio as MN

tipo_save  = "temporal"

def view_tiposave(request):
    if request.is_ajax():
        if request.method == 'POST':
            tipo_save = request.POST['ts']
    return

def view_bringmunicipio(request):
    
    if request.is_ajax():
        if request.GET['data'] == 'muns':
            try:
                muns = MN.FilterByDep(request.GET['iddep'])
                #muns = MN.objects.filter(departamento = request.GET['iddep'])
                #print muns
                data = [{'pk':m.pk,'descripcion':m.nombre} for m in muns]
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            except Exception,e:
                print e
                return HttpResponse('MAL')
            else:
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            
def view_bringcentros(request):
    
    if request.is_ajax():
        if request.GET['data'] == 'centros':
            try:
                idmun = request.GET['idmun']
                iddep = MN.BringDepId(idmun)
                
                centros = CE.FilterByDepMun(iddep,idmun)
                data = [{'pk':c.pk,'descripcion':c.nombre} for c in centros]
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            except Exception,e:
                print e
                return HttpResponse('MAL')
            else:
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def view_save(request,pg,encuesta_id):
    
    if tipo_save == "temporal":
        encuesta = ET.objects.get(pk=encuesta_id)
    #else:
     #   encuesta = T.objects.get(pk=encuesta_id)    
    if pg == "pg1":
        
        infoC=SC.BringAll()
        infoD=SD.BringAll()
        
        SaveBasic(request.POST['cbx_centros'],request.POST['tbx_fecha'],tipo_save,encuesta_id)
        SavePartA(request,tipo_save,encuesta)
        SavePartB(request,tipo_save,encuesta)
        SavePartC(request,infoC,tipo_save,encuesta)
        SavePartD(request,infoD,tipo_save,encuesta)

    else :
        
        infoE= SE.BringAll()
        infoG= SG.BringAll()
        
        SavePartE(request,infoE,tipo_save,encuesta)
        SavePartF(request,tipo_save,encuesta)
        SavePartG(request,infoG,tipo_save,encuesta)
        
    return HttpResponse('Encuesta temp guardada')   

def SaveBasic(codigo_centro,fecha,tipo_guardar,codigo_tabla):
    
    if tipo_guardar == "temporal":
        ET.objects.filter(codigo = codigo_tabla).update(fecha=fecha,codigo_centro = codigo_centro)

        
def SavePartA(datos,tipo_guardar,encuesta):
    if tipo_guardar == "temporal":
        obj02 = SA.objects.get(descripcion = datos)
        row=ETD(encuesta = encuesta,segmento="A",codigo_item=obj02.codigo,tipo_valor="texto",valor_item = datos)
        row.save()

def SavePartB(datos,tipo_guardar,encuesta):
    
    if tipo_guardar == "temporal":
        lista = datos.POST.getlist("cbxB")
        lista2 = datos.POST.getlist("tbx_oi")
    
        for l in lista:
            obj = SB.objects.get(pk=l)
            row=ETD(encuesta = encuesta,segmento="B",codigo_item=l,tipo_valor="seleccion",valor_item = obj.descripcion)
            row.save()
        for l2 in lista2:
            if l2 != "":
                row=ETD(encuesta = encuesta,segmento="B",codigo_item=-1,tipo_valor="extra",valor_item = l2)
                row.save()
    
def SavePartC(datos,items,tipo_guardar,encuesta):
    
    if tipo_guardar == "temporal":
        for i in items:
            string = "selC_" + str(i.codigo)
            obj = datos.POST[string]
            row=ETD(encuesta = encuesta,segmento="C",codigo_item=i.codigo,tipo_valor="opcion",valor_item = obj)
            row.save()        
    
def SavePartD(datos,items,tipo_guardar,encuesta):

    if tipo_guardar == "temporal":
        for i in items:
            string = "tbxD_" + str(i.codigo)
            obj = datos.POST[string]
            row = ETD(encuesta=encuesta,segmento="D",codigo_item=i.codigo,tipo_valor="numerico",valor_item=obj)
            row.save()
        
def SavePartE(datos,items,tipo_guardar,encuesta):
    
    if tipo_guardar == "temporal":
        for i in items:
            string = "tbxE_" + str(i.codigo)
            obj = datos.POST[string]
            row = ETD(encuesta=encuesta,segmento="E",codigo_item=i.codigo,tipo_valor="numerico",valor_item=obj)
            row.save()
            
def SavePartF(datos,tipo_guardar,encuesta):
    
    if tipo_guardar == "temporal":
        lista = datos.POST.getlist("cbxF")
        lista2 = datos.POST.getlist("tbx_oi2")
        for l in lista:
            print l
            obj = SF.objects.get(pk=l)
            row=ETD(encuesta = encuesta,segmento="F",codigo_item=l,tipo_valor="seleccion",valor_item = obj.descripcion)
            row.save()

        for l2 in lista2:
            if l2 != "":
                row=ETD(encuesta = encuesta,segmento="F",codigo_item=-1,tipo_valor="extra",valor_item = l2)
                row.save()
def SavePartG(datos,items,tipo_guardar,encuesta):
    
    if tipo_guardar == "temporal":
        for i in items:
            string = "selG_" + str(i.codigo)
            obj = datos.POST[string]
            row=ETD(encuesta = encuesta,segmento="G",codigo_item=i.codigo,tipo_valor="opcion",valor_item = obj)
            row.save()
                   
def view_encuesta(request,tipo):
    
    usuario = request.user
    username = usuario.username
    userid = usuario.id
    
    infoA= SA.BringAll()
    infoB= SB.BringAll()
    infoC= SC.BringAll()
    infoD= SD.BringAll()
    infoE= SE.BringAll()
    infoF= SF.BringAll()
    infoG= SG.BringAll()
        
    centros = CE.BringAll()
    deps = DP.BringAll()
    muns= MN.BringAll()
        
    if tipo == "nueva":
        p = ET(codigo_usuario=request.user)
        p.save()
             
        return render_to_response('Encuesta.html',{'usuario':username,'id_usuario':userid,'codigo_enc':p.codigo,'tipo_save':tipo_save,'deps':deps,'centros':centros,'infoA':infoA,'infoB':infoB,'infoC':infoC,'infoD':infoD,'infoE':infoE,'infoF':infoF,'infoG':infoG,'muns':muns},context_instance=RequestContext(request))
    else:
        HttpResponse("hola")

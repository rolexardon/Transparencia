from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.utils import simplejson
from datetime import datetime as dt

from Encuesta.models import SegmentoA as SA
from Encuesta.models import SegmentoB as SB
from Encuesta.models import SegmentoC as SC
from Encuesta.models import SegmentoD as SD
from Encuesta.models import SegmentoE as SE
from Encuesta.models import SegmentoF as SF
from Encuesta.models import SegmentoG as SG
from Encuesta.models import Encuesta as E
from Encuesta.models import EncuestaData as ED
from Encuesta.models import EncuestaTemp as ET
from Encuesta.models import EncuestaTempData as ETD

from Administration.models import CentroEducativo as CE
from Administration.models import Departamento as DP
from Administration.models import Municipio as MN

from Transparencia.views import PrepareContent

tipo_save  = ""
id_encuestafinal = 0

def view_bringmunicipio(request):
    
    if request.is_ajax():
        if request.GET['data'] == 'muns':
            try:
                muns = MN.FilterByDep(request.GET['iddep'])
                data = [{'pk':m.codigo,'descripcion':m.nombre} for m in muns]
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            except Exception,e:
                print e
                return HttpResponse('Error')
            else:
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            
def view_bringcentros(request):
    
    if request.is_ajax():
        if request.GET['data'] == 'centros':
            try:
                idmun = request.GET['idmun']
                #iddep = MN.BringDepId(idmun)
                iddep = request.GET['iddep']
                centros = CE.FilterByDepMun(iddep,idmun)
                data = [{'pk':c.pk,'descripcion':c.nombre + "(" + c.direccion + ")"} for c in centros]
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            except Exception,e:
                print e
                return HttpResponse('Error')
            else:
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            

def view_bringcentroinfo(request):
    
    if request.is_ajax():
        if request.GET['data'] == 'infodecentro':
            try:
                idcentro = request.GET['idcentro']
                codigo = CE.GetCodigoCentro(idcentro)
                tipo = CE.GetTipoCentro(idcentro)
                resp = [codigo,tipo]
                return HttpResponse(simplejson.dumps(resp), mimetype="application/json")
            except Exception,e:
                print e
                return HttpResponse('Error')
            else:
                return HttpResponse(simplejson.dumps(resp), mimetype="application/json")
            
            
def view_save(request,pg,encuesta_id):
    if pg == "pg1":
        tipo_save = request.POST['tipo_save']
        if tipo_save == "temporal":
            encuesta = ET.objects.get(pk=encuesta_id)
            SaveBasic(request,encuesta_id)
            ETD.objects.filter(encuesta= encuesta_id).delete()
        else:
            encuesta = SaveBasic(request,-1)
            
        infoC=SC.BringAll()
        infoD=SD.BringAll()
        SavePartA(request.POST['cbx_parteA'],tipo_save,encuesta)
        SavePartB(request,tipo_save,encuesta)
        SavePartC(request,infoC,tipo_save,encuesta)
        SavePartD(request,infoD,tipo_save,encuesta)

    else :
        tipo_save = request.POST['tipo_save']
        if tipo_save == "temporal":
            encuesta = ET.objects.get(pk=encuesta_id)
        else:
            p = E.objects.latest('codigo')
            encuesta = E.objects.get(pk= p.codigo)
            
        infoE= SE.BringAll()
        infoG= SG.BringAll()
        SavePartE(request,infoE,tipo_save,encuesta)
        SavePartF(request,tipo_save,encuesta)
        SavePartG(request,infoG,tipo_save,encuesta)
        
    borrar_temporal(encuesta_id,request.POST['tipo_save'])    
    return PrepareContent(request.user,request)

def SaveBasic(datos,codigo_tabla):
    try:
        if codigo_tabla != -1 :
            p = ET.objects.filter(codigo = codigo_tabla)
            if 'tbx_fecha' in datos.POST:
                fecha=datos.POST['tbx_fecha']
                if fecha != "":
                    p.update(fecha=fecha)
            if 'cbx_centros' in datos.POST:
                centro=datos.POST['cbx_centros']
                p.update(codigo_centro = centro)
            if 'tbx_tel1' in datos.POST:
                t1=datos.POST['tbx_tel1']
                if t1 != "":
                    p.update(tel=t1)
                else :
                    p.update(tel=None)
            zona = datos.POST['cbx_zonacentro']
            p.update(zona=zona)
        else :
            departamento = DP.objects.get(pk=datos.POST['cbx_dep'])
            municipio = MN.objects.get(pk=datos.POST['cbx_mun'])
            centro = CE.objects.get(pk=datos.POST['cbx_centros'])
            fecha = datos.POST['tbx_fecha']
            zona = datos.POST['cbx_zonacentro']
            t1=datos.POST['tbx_tel1']
            
            row=E(codigo_usuario = datos.user,fecha=fecha,codigo_departamento = departamento, codigo_municipio = municipio, codigo_centro = centro,zona=zona,tel=t1,fecha_apertura = dt.today())
            row.save()
            return row   
    except Exception as inst:     
        print inst

def SavePartA(item,tipo_guardar,encuesta):
    
    obj02 = SA.objects.get(descripcion = item )
    if tipo_guardar == "temporal":
        row=ETD(encuesta = encuesta,segmento="A",codigo_item=obj02.codigo,tipo_valor="texto",valor_item = item)
    else:
        row=ED(encuesta = encuesta,segmento="A",codigo_item=obj02.codigo,tipo_valor="texto",valor_item = item)
    row.save()

def SavePartB(datos,tipo_guardar,encuesta):
    
    lista = datos.POST.getlist("cbxB")
    lista2 = datos.POST.getlist("tbx_oi")
    
    if tipo_guardar == "temporal":

        for l in lista:
            obj = SB.objects.get(pk=l)
            row=ETD(encuesta = encuesta,segmento="B",codigo_item=l,tipo_valor="seleccion",valor_item = obj.descripcion)
            row.save()
        for l2 in lista2:
            if l2 != "":
                row=ETD(encuesta = encuesta,segmento="B",codigo_item=-1,tipo_valor="extra",valor_item = l2)
                row.save()
    else:

        for l in lista:
            obj = SB.objects.get(pk=l)
            row=ED(encuesta = encuesta,segmento="B",codigo_item=l,tipo_valor="seleccion",valor_item = obj.descripcion)
            row.save()
        for l2 in lista2:
            if l2 != "":
                row=ED(encuesta = encuesta,segmento="B",codigo_item=-1,tipo_valor="extra",valor_item = l2)
                row.save()       
        
    
def SavePartC(datos,items,tipo_guardar,encuesta):
    
    if tipo_guardar == "temporal":
        for i in items:
            string = "selC_" + str(i.codigo)
            obj = datos.POST[string]
            row=ETD(encuesta = encuesta,segmento="C",codigo_item=i.codigo,tipo_valor="opcion",valor_item = obj)
            row.save()
    else:
        for i in items:
            string = "selC_" + str(i.codigo)
            obj = datos.POST[string]
            row=ED(encuesta = encuesta,segmento="C",codigo_item=i.codigo,tipo_valor="opcion",valor_item = obj)
            row.save()
    
def SavePartD(datos,items,tipo_guardar,encuesta):

    if tipo_guardar == "temporal":
        for i in items:
            string = "tbxD_" + str(i.codigo)
            obj = datos.POST[string]
            if obj != "":
                row = ETD(encuesta=encuesta,segmento="D",codigo_item=i.codigo,tipo_valor="numerico",valor_item=obj)
                row.save()
    else:
        for i in items:
            string = "tbxD_" + str(i.codigo)
            obj = datos.POST[string]
            if obj != "":
                row = ED(encuesta=encuesta,segmento="D",codigo_item=i.codigo,tipo_valor="numerico",valor_item=obj)
                row.save()        
        
def SavePartE(datos,items,tipo_guardar,encuesta):
    
    if tipo_guardar == "temporal":
        for i in items:
            string = "tbxE_" + str(i.codigo)
            obj = datos.POST[string]
            if obj != "":
                row = ETD(encuesta=encuesta,segmento="E",codigo_item=i.codigo,tipo_valor="numerico",valor_item=obj)
                row.save()
    else:
        for i in items:
            string = "tbxE_" + str(i.codigo)
            obj = datos.POST[string]
            if obj != "":
                row = ED(encuesta=encuesta,segmento="E",codigo_item=i.codigo,tipo_valor="numerico",valor_item=obj)
                row.save()
            
def SavePartF(datos,tipo_guardar,encuesta):
    
    lista = datos.POST.getlist("cbxF")
    lista2 = datos.POST.getlist("tbx_oi2")
    if tipo_guardar == "temporal":

        for l in lista:
            obj = SF.objects.get(pk=l)
            row=ETD(encuesta = encuesta,segmento="F",codigo_item=l,tipo_valor="seleccion",valor_item = obj.descripcion)
            row.save()

        for l2 in lista2:
            if l2 != "":
                row=ETD(encuesta = encuesta,segmento="F",codigo_item=-1,tipo_valor="extra",valor_item = l2)
                row.save()
    else:
        for l in lista:
            obj = SF.objects.get(pk=l)
            row=ED(encuesta = encuesta,segmento="F",codigo_item=l,tipo_valor="seleccion",valor_item = obj.descripcion)
            row.save()

        for l2 in lista2:
            if l2 != "":
                row=ED(encuesta = encuesta,segmento="F",codigo_item=-1,tipo_valor="extra",valor_item = l2)
                row.save()
        
def SavePartG(datos,items,tipo_guardar,encuesta):
    
    if tipo_guardar == "temporal":
        for i in items:
            string = "selG_" + str(i.codigo)
            obj = datos.POST[string]
            row=ETD(encuesta = encuesta,segmento="G",codigo_item=i.codigo,tipo_valor="opcion",valor_item = obj)
            row.save()
    else:
        for i in items:
            string = "selG_" + str(i.codigo)
            obj = datos.POST[string]
            row=ED(encuesta = encuesta,segmento="G",codigo_item=i.codigo,tipo_valor="opcion",valor_item = obj)
            row.save()
                   
def borrar_temporal(encuesta, borrar):
    if borrar == "final":
        enc = ET.objects.filter(pk=encuesta)
        enc.delete()
    
        enc_data = ETD.objects.filter(encuesta = encuesta)
        enc_data.delete()
    
def view_encuesta(request,encuesta):
    
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
        
    if encuesta == "nueva":
        p = ET(codigo_usuario=request.user,fecha_apertura = dt.today())
        print request.user
        p.save()
        print "jola"
        today = dt.today()
        
        showbtns = True
        return render_to_response('Encuesta.html',{'usuario':username,'id_usuario':userid,'codigo_enc':p.codigo,'tipo_save':tipo_save,'deps':deps,'centros':centros,'infoA':infoA,'infoB':infoB,'infoC':infoC,'infoD':infoD,'infoE':infoE,'infoF':infoF,'infoG':infoG,'muns':muns,'tipo':"nueva", 'range1':range(4),'range2':range(3),'today':today,'show':showbtns},context_instance=RequestContext(request))
    else:
        e = ET.objects.get(pk=encuesta)
        #data = ETD.objects.filter(encuesta=e)
    
        data_a = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "A").values())
        data_b = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "B",tipo_valor="seleccion").values())
        data_b2 = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "B",tipo_valor="extra").values())
        data_c = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "C").values())
        data_d = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "D").values())
        data_e = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "E").values())
        data_f = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "F",tipo_valor="seleccion").values())
        data_f2 = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "F",tipo_valor="extra").values())
        data_g = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "G").values())
        
        #data_a = data_a[0].get('codigo_item')
        data_a = GetList(data_a,1)
        data_b = GetList(data_b,1)
        data_b2 = GetList(data_b2,2)
        data_c = GetList(data_c,2)
        data_d = GetList(data_d,2) 
        data_e = GetList(data_e,2)
        data_f = GetList(data_f,1)
        data_f2 = GetList(data_f2,2)
        data_g = GetList(data_g,2)        
        
        data_b2 = CompleteSpaces(data_b2,4)
        data_f2 = CompleteSpaces(data_f2,3)
        data_d = CompleteSpaces(data_d,len(infoD))
        data_e = CompleteSpaces(data_e,len(infoE))
        
        showbtns = True
        return render_to_response('Encuesta.html',{'usuario':username,'id_usuario':userid,'codigo_enc':encuesta,'tipo_save':tipo_save,'deps':deps,'centros':centros,'infoA':infoA,'infoB':infoB,'infoC':infoC,'infoD':infoD,'infoE':infoE,'infoF':infoF,'infoG':infoG,'muns':muns,'tipo':"existente",'encuesta':e, 'da':data_a, 'db':data_b,'db2':data_b2, 'dc':data_c, 'dd':data_d, 'de':data_e, 'df':data_f, 'df2':data_f2,'dg':data_g, 'range': range(4),'show':showbtns},context_instance=RequestContext(request))

def view_publicadas(request,encuesta):
    
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
        
    e = E.objects.get(pk=encuesta)
    #data = ETD.objects.filter(encuesta=e)

    data_a = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "A").values())
    data_b = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "B",tipo_valor="seleccion").values())
    data_b2 = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "B",tipo_valor="extra").values())
    data_c = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "C").values())
    data_d = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "D").values())
    data_e = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "E").values())
    data_f = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "F",tipo_valor="seleccion").values())
    data_f2 = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "F",tipo_valor="extra").values())
    data_g = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "G").values())
    
    #data_a = data_a[0].get('codigo_item')
    data_a = GetList(data_a,1)
    data_b = GetList(data_b,1)
    data_b2 = GetList(data_b2,2)
    data_c = GetList(data_c,2)
    data_d = GetList(data_d,2) 
    data_e = GetList(data_e,2)
    data_f = GetList(data_f,1)
    data_f2 = GetList(data_f2,2)
    data_g = GetList(data_g,2)        
    
    data_b2 = CompleteSpaces(data_b2,4)
    data_f2 = CompleteSpaces(data_f2,3)
    data_d = CompleteSpaces(data_d,len(infoD))
    data_e = CompleteSpaces(data_e,len(infoE))
    
    showbtns = False
    return render_to_response('Encuesta.html',{'usuario':username,'id_usuario':userid,'codigo_enc':encuesta,'tipo_save':tipo_save,'deps':deps,'centros':centros,'infoA':infoA,'infoB':infoB,'infoC':infoC,'infoD':infoD,'infoE':infoE,'infoF':infoF,'infoG':infoG,'muns':muns,'tipo':"existente",'encuesta':e, 'da':data_a, 'db':data_b,'db2':data_b2, 'dc':data_c, 'dd':data_d, 'de':data_e, 'df':data_f, 'df2':data_f2,'dg':data_g, 'range': range(4),'show':showbtns},context_instance=RequestContext(request))

def ConvertToDict(valuesqueryset):
    return [item for item in valuesqueryset]
def GetList(data,tipo):
    if tipo == 1:
        lista = list(item.get('codigo_item') for item in data)
    else:
        lista = list(item.get('valor_item') for item in data)   
    return lista
def CompleteSpaces(data,cantidad):
    
    existentes = len(data)
    agrega = cantidad - existentes
    rg = range(agrega)
    
    for n in rg:
        data.append("")
    
    return data
        

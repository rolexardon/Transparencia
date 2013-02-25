from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.utils import simplejson
from datetime import datetime as dt
from django.db import transaction
from django.contrib.auth.models import User
from datetime import datetime
from Encuesta.models import SegmentoA as SA
from Encuesta.models import SegmentoB as SB
from Encuesta.models import SegmentoC as SC
from Encuesta.models import SegmentoD as SD
from Encuesta.models import SegmentoE as SE
from Encuesta.models import SegmentoF as SF
from Encuesta.models import SegmentoG as SG
from Encuesta.models import Encuesta
from Encuesta.models import EncuestaData as ED
from Encuesta.models import EncuestaTemp as ET
from Encuesta.models import EncuestaTempData as ETD
from Encuesta.models import ListadoDocentesTemp as LDT
from Encuesta.models import ListadoDocentes as LD
from Administration.models import CentroEducativo as CE
from Administration.models import Departamento as DP
from Administration.models import Municipio as MN
from Transparencia.views import PrepareContent
from Encuesta.forms import ET_Form, E_Form
from PIL import Image as PImage
from os.path import join as pjoin
import os
ROOT_PATH =  os.path.dirname(__file__)
from Transparencia.settings import MEDIA_ROOT
from dateutil import parser


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
                return HttpResponse(e)
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
                return HttpResponse(e)
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
                return HttpResponse(e)
            else:
                return HttpResponse(simplejson.dumps(resp), mimetype="application/json")

def view_save(request,encuesta_id):    
	
    try:
        tipo_save = request.POST['tipo_save']
        if tipo_save == "temporal":
            SaveBasic(request,encuesta_id,tipo_save)
            if request.method == "POST":
                encuesta = ET.objects.get(pk=encuesta_id)
                if 'imagen01' in request.FILES:
                    if encuesta.imagen01:
                        os.remove(encuesta.imagen01.path)
                if 'imagen02' in request.FILES:
                    if encuesta.imagen02:
                        os.remove(encuesta.imagen02.path)
                    
                etf = ET_Form(request.POST, request.FILES, instance = encuesta)
                if etf.is_valid():
                    etf.save()

                    # resize and save image under same filename
 
            #ETD.objects.filter(encuesta= encuesta_id).delete()
            ETD.objects.filter(encuesta= encuesta).delete()

        else:

            encuesta = SaveBasic(request,encuesta_id,tipo_save)
            SaveDocentesPartE(encuesta_id,encuesta)
        infoC=SC.BringAll()
        infoD=SD.BringAll()
        SavePartA(request,tipo_save,encuesta)
        SavePartB(request,tipo_save,encuesta)
        SavePartC(request,infoC,tipo_save,encuesta)
        SavePartD(request,infoD,tipo_save,encuesta)

    #else :
     #   if tipo_save == "temporal":
      #      encuesta = ET.objects.get(pk=encuesta_id)
       # else:
        #    encuesta = E.objects.latest('codigo')
         #   SaveDocentesPartE(encuesta_id,encuesta)

        infoE= SE.BringAll()
        infoG= SG.BringAll()
        SavePartE(request,infoE,tipo_save,encuesta)
        SavePartF(request,tipo_save,encuesta)
        SavePartG(request,infoG,tipo_save,encuesta)
        borrar_temporal(encuesta_id,tipo_save)


        return PrepareContent(request.user,request)
    except Exception, e :
        return HttpResponse(e)

def SaveDocentesPartE(encuesta_temporal,encuesta_final):
    try:
        temporal = ET.objects.get(codigo = encuesta_temporal)
        docentes = LDT.objects.filter(encuesta = temporal)
        for do in docentes:
            object = LD(encuesta=encuesta_final,segmento=do.segmento,id_personal = do.id_personal, nombre = do.nombre)
            object.save()
    except Exception,e:
        return HttpResponse(e)

def SaveBasic(datos,codigo_tabla,ts):
    try:
        if ts == "temporal":
            p = ET.objects.get(codigo = codigo_tabla)
            if 'tbx_fecha' in datos.POST:
                fecha=datos.POST['tbx_fecha']
                if fecha != "":
					#valid_fecha = datetime.strptime(fecha, '%d/%m/%Y')
					#p.fecha = fecha
					dt = parser.parse(fecha)
					#p.update(fecha=dt)
					p.fecha = dt
					#p.save()
            if 'cbx_centros' in datos.POST:
                centro=datos.POST['cbx_centros']
                centro=CE.objects.get(pk=centro)
                p.codigo_centro = centro
				#p.update(codigo_centro = centro)
            if 'tbx_tel1' in datos.POST:
                t1=datos.POST['tbx_tel1']
                if t1 != "":
                    #p.update(tel=t1)
					p.tel = t1
                else :
                    #p.update(tel=None)
					p.tel=None
            if 'tbx_obsv' in datos.POST:
                ob = datos.POST['tbx_obsv']
                #p.update(observacion= ob)
                p.observacion=ob
            if 'tbx_alumnos' in datos.POST:
                ob = datos.POST['tbx_alumnos']
                if ob != "":
                    #p.update(alumnos=ob)
                    p.alumnos = ob
                else :
                    #p.update(alumnos=None)
                    p.alumnos=None
            zona = datos.POST['cbx_zonacentro']
            #p.update(zona=zona)
            p.zona=zona
                
            p.save()
            
        else:
            encuesta_temp = ET.objects.get(pk=codigo_tabla)
            etf = ET_Form(datos.POST, datos.FILES, instance = encuesta_temp)
            if etf.is_valid():
                etf.save()
            img1 = encuesta_temp.imagen01
            img2 = encuesta_temp.imagen02
            
            departamento = DP.objects.get(pk=datos.POST['cbx_dep'])
            municipio = MN.objects.get(pk=datos.POST['cbx_mun'])
            centro = CE.objects.get(pk=datos.POST['cbx_centros'])
            
            fecha=datos.POST['tbx_fecha']
            if fecha != "":
                dt = parser.parse(fecha)
                fecha = dt
                
            zona = datos.POST['cbx_zonacentro']
            t1=datos.POST['tbx_tel1']
            al = datos.POST['tbx_alumnos']
            if 'tbx_obsv' in datos.POST:
                ob = datos.POST['tbx_obsv']
            else: ob = ""
            try:
                 row=Encuesta(codigo_usuario = datos.user,fecha=fecha,codigo_departamento = departamento, codigo_municipio = municipio, codigo_centro = centro,zona=zona,tel=t1,fecha_apertura = dt.today(),observacion = ob,alumnos = al,imagen01 = img1, imagen02 = img2)
                 row.save()
            except Exception,e:
                 HttpResponse(e)
        return row
    except Exception,e:
        return HttpResponse(e)

def SavePartA(item,tipo_guardar,encuesta):
    try:
        item2 = item.POST['cbx_parteA']
        obj02 = SA.objects.get(codigo = item2 )
        obj02_str = str(obj02)
        if tipo_guardar == "temporal":
            if "Otra" in obj02_str:
                otra = item.POST['tbx_otraubi']
                if otra == "":
                    otra="pending"
                row=ETD(encuesta = encuesta,segmento="A",codigo_item=obj02.codigo,tipo_valor="texto",valor_item = obj02_str)
                row=ETD(encuesta = encuesta,segmento="A",codigo_item=obj02.codigo,tipo_valor="extra",valor_item = otra)
            else:
                row=ETD(encuesta = encuesta,segmento="A",codigo_item=obj02.codigo,tipo_valor="texto",valor_item = obj02_str)
        else:
            if "Otra" in item2:
                otra = item.POST['tbx_otraubi']
                row=ED(encuesta = encuesta,segmento="A",codigo_item=obj02.codigo,tipo_valor="texto",valor_item = obj02_str)
                row=ED(encuesta = encuesta,segmento="A",codigo_item=obj02.codigo,tipo_valor="extra",valor_item = otra)
            else:
                row=ED(encuesta = encuesta,segmento="A",codigo_item=obj02.codigo,tipo_valor="texto",valor_item = obj02_str)
        row.save()
    except Exception,e:
        return HttpResponse(e)

def SavePartB(datos,tipo_guardar,encuesta):
    try:
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
    except Exception,e:
        return HttpResponse(e)


def SavePartC(datos,items,tipo_guardar,encuesta):
    try:
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
    except Exception,e:
        return HttpResponse(e)

def SavePartD(datos,items,tipo_guardar,encuesta):
    try:
        if tipo_guardar == "temporal":
            for i in items:
                string = "tbxD_" + str(i.codigo)
                obj = datos.POST[string]
                if obj == "":
                    obj=0
                row = ETD(encuesta=encuesta,segmento="D",codigo_item=i.codigo,tipo_valor="numerico",valor_item=obj)
                row.save()
        else:
            for i in items:
                string = "tbxD_" + str(i.codigo)
                obj = datos.POST[string]
                if obj == "":
                    obj=0
                row = ED(encuesta=encuesta,segmento="D",codigo_item=i.codigo,tipo_valor="numerico",valor_item=obj)
                row.save()
    except Exception,e:
        return HttpResponse(e)

def SavePartE(datos,items,tipo_guardar,encuesta):
    try:
        rows = ETD.objects.filter(encuesta= encuesta, segmento = "E")
        rows.delete()
        for i in items:
            string = "tbxE_" + str(i.codigo)
            obj = datos.POST[string]
            if obj == "":
                obj=0
            if tipo_guardar == "temporal":
                row = ETD(encuesta=encuesta,segmento="E",codigo_item=i.codigo,tipo_valor="numerico",valor_item=obj)
                row.save()
            else:
                row = ED(encuesta=encuesta,segmento="E",codigo_item=i.codigo,tipo_valor="numerico",valor_item=obj)
                row.save()
    except Exception,e:
        return HttpResponse(e)

def SavePartF(datos,tipo_guardar,encuesta):
    try:
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
    except Exception,e:
        return HttpResponse(e)

def SavePartG(datos,items,tipo_guardar,encuesta):
    try:
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
    except Exception,e:
        return HttpResponse(e)

def borrar_temporal(encuesta, borrar):
    if borrar == "final":
        enc = ET.objects.get(codigo=encuesta)
        enc.delete()

        enc_data = ETD.objects.filter(encuesta = encuesta)
        enc_data.delete()


def view_encuesta(request,encuesta):
    try:
        usuario = request.user
        username = usuario.username
        userid = usuario.id
        codigo_usuario = User.objects.get(id = userid)

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
            today = dt.now()
            p = ET(codigo_usuario=codigo_usuario,fecha_apertura = today)
            p.save()
            showbtns = True

            etf = ET_Form(instance=p)

            #fecha = dt.now()

            #fecha = d % '-' % m % '-' % y
            #print fecha
            return render_to_response('Encuesta.html',{'usuario':username,'id_usuario':userid,'codigo_enc':p.codigo,'tipo_save':tipo_save,'deps':deps,'centros':centros,'infoA':infoA,'infoB':infoB,'infoC':infoC,'infoD':infoD,'infoE':infoE,'infoF':infoF,'infoG':infoG,'muns':muns,'tipo':"nueva", 'range1':range(4),'range2':range(3),'today':today,'show':showbtns,'etf':etf},context_instance=RequestContext(request))
        else:
            
            #fecha = d % '-' % m % '-' % y
            #print fecha
            e = ET.objects.get(pk=encuesta)
            #today = str(e.fecha)
            
            today = e.fecha
            #dt = parser.parse(today)
            #today = dt
            if today:
                today= today.strftime('%d/%m/%y')
            else:
                today=""
            etf = ET_Form(instance=e)

            #data = ETD.objects.filter(encuesta=e)

            data_a = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "A").values())
            data_a2 = ConvertToDict(ETD.objects.filter(encuesta=e,segmento = "A",tipo_valor="extra").values())
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
            data_a2 = GetList(data_a2,2)
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
            return render_to_response('Encuesta.html',{'usuario':username,'id_usuario':userid,'codigo_enc':encuesta,'tipo_save':tipo_save,'deps':deps,'centros':centros,'infoA':infoA,'infoB':infoB,'infoC':infoC,'infoD':infoD,'infoE':infoE,'infoF':infoF,'infoG':infoG,'muns':muns,'tipo':"existente",'encuesta':e, 'da':data_a,'da2':data_a2, 'db':data_b,'db2':data_b2, 'dc':data_c, 'dd':data_d, 'de':data_e, 'df':data_f, 'df2':data_f2,'dg':data_g, 'range': range(4),'show':showbtns,'today':today,'etf':etf},context_instance=RequestContext(request))
    except Exception,e:
        return HttpResponse(e)

def view_publicadas(request,encuesta):
    #try:
    usuario = request.user.pk
    username = request.user.username
    userid = request.user.id

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

    e = Encuesta.objects.get(pk=encuesta)
    today = str(e.fecha)
    #data = ETD.objects.filter(encuesta=e)
    
    etf = E_Form(instance=e)

    data_a = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "A").values())
    data_a2 = ConvertToDict(ED.objects.filter(encuesta=e,segmento = "A",tipo_valor="extra").values())
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
    data_a2 = GetList(data_a2,2)
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
    return render_to_response('Encuesta.html',{'usuario':username,'id_usuario':userid,'codigo_enc':encuesta,'tipo_save':tipo_save,'deps':deps,'centros':centros,'infoA':infoA,'infoB':infoB,'infoC':infoC,'infoD':infoD,'infoE':infoE,'infoF':infoF,'infoG':infoG,'muns':muns,'tipo':"existente",'encuesta':e, 'da':data_a,'da2':data_a2, 'db':data_b,'db2':data_b2, 'dc':data_c, 'dd':data_d, 'de':data_e, 'df':data_f, 'df2':data_f2,'dg':data_g, 'range': range(4),'show':showbtns,'today':today,'etf':etf},context_instance=RequestContext(request))
    #except Exception,e:
       # return HttpResponse(e)

def ConvertToDict(valuesqueryset):
    try:
        return [item for item in valuesqueryset]
    except Exception,e:
        return HttpResponse(e)

def GetList(data,tipo):
    try:
        if tipo == 1:
            lista = list(item.get('codigo_item') for item in data)
        else:
            lista = list(item.get('valor_item') for item in data)
        return lista

    except Exception,e:
        return HttpResponse(e)

def CompleteSpaces(data,cantidad):
    try:
        existentes = len(data)
        agrega = cantidad - existentes
        rg = range(agrega)

        for n in rg:
            data.append("")

        return data
    except Exception,e:
        return HttpResponse(e)

def view_borrartemporal(request):
    if request.is_ajax():
        if request.GET['data'] == 'delete':
            try:
                encuesta = ET.objects.get(codigo = request.GET['idenc'])
                #encuesta = request.GET['idenc']
                #ETD.objects.raw("DELETE FROM Encuesta_encuestatempdata WHERE encuesta = " + encuesta)
                #p = ETD(encuesta = encuesta)
                #p.delete()
                #ET.objects.raw("DELETE FROM Encuesta_encuestatemp WHERE codigo = " + encuesta)
                #p2 = ET(encuesta = encuesta)
                #p2.delete()
                try:
                    os.remove(encuesta.imagen01.path)
                    os.remove(encuesta.imagen02.path)
                except Exception,e:
                    pass
                encuesta.delete()
                #return PrepareContent(request.user,request)
                data = "listo"
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            except Exception,e:

                return HttpResponse(e)
            else:
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def view_rethome(request):
    return PrepareContent(request.user,request)

def view_adddocente(request,encuesta):
    if request.is_ajax():
        if request.GET['data'] == 'save':
            try:
                id = request.GET['id']
                name = request.GET['name']
                encuesta_id = request.GET['enc']
                segmento = request.GET['seg']
                encuesta = ET.objects.get(codigo = encuesta_id)

                registro = LDT(encuesta = encuesta,segmento = segmento,id_personal = id,nombre = name)
                registro.save()

                docentes = LDT.BringAll(encuesta,segmento)
                data = [{'pk':d.id_personal,'nombre':d.nombre} for d in docentes]

                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            except Exception,e:
                return HttpResponse(e)
            else:
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
        else:
            if request.GET['data'] == 'erase':
                try:
                    texto = request.GET['texto']
                    encuesta_id = request.GET['enc']
                    segmento = request.GET['seg']
                    encuesta = ET.objects.get(codigo = encuesta_id)

                    list = texto.split('~')
                    id = list[0]
                    name = list[1]

                    registro = LDT.objects.get(encuesta = encuesta,segmento = segmento,id_personal = id,nombre = name)
                    registro.delete()

                    docentes = LDT.BringAll(encuesta,segmento)
                    data = [{'pk':d.id_personal,'nombre':d.nombre} for d in docentes]

                    return HttpResponse(simplejson.dumps(data), mimetype="application/json")
                except Exception,e:
                    return HttpResponse(e)
                else:
                    return HttpResponse(simplejson.dumps(data), mimetype="application/json")

            else:
                try:
                    segmento = request.GET['seg']
                    encuesta_id = request.GET['enc']
                    estemp = request.GET['temp']

                    if estemp == 'True':
                        encuesta = ET.objects.get(codigo = encuesta_id)
                        docentes = LDT.BringAll(encuesta,segmento)
                        data = [{'pk':d.id_personal,'nombre':d.nombre} for d in docentes]
                    else:
                        encuesta = Encuesta.objects.get(codigo = encuesta_id)
                        docentes = LD.BringAll(encuesta,segmento)
                        data = [{'pk':d.id_personal,'nombre':d.nombre} for d in docentes]


                    return HttpResponse(simplejson.dumps(data), mimetype="application/json")
                except Exception,e:
                    return HttpResponse(e)
                else:
                    return HttpResponse(simplejson.dumps(data), mimetype="application/json")

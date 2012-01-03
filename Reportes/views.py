from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.utils import simplejson

import string

from django.contrib.auth.models import User
from Administration.models import Usuario as U 
from Administration.models import TipoUsuario as TU
from Administration.models import Departamento as DP

from Encuesta.models import SegmentoA as SA
from Encuesta.models import SegmentoB as SB
from Encuesta.models import SegmentoC as SC
from Encuesta.models import SegmentoD as SD
from Encuesta.models import SegmentoE as SE
from Encuesta.models import SegmentoF as SF
from Encuesta.models import SegmentoG as SG

from Encuesta.models import Encuesta as E

def view_reporte(request):
    
    usuarios = User.objects.all
    tipos = TU.BringAll()
    deps = DP.BringAll()
    
    infoA= SA.BringAll()
    infoB= SB.BringAll()
    infoC= SC.BringAll()
    infoD= SD.BringAll()
    infoE= SE.BringAll()
    infoF= SF.BringAll()
    infoG= SG.BringAll()
    
    return render_to_response('Reportes.html',{'usuarios':usuarios,'tipos':tipos, 'deps':deps,'infoA':infoA,'infoB':infoB,'infoC':infoC,'infoD':infoD,'infoE':infoE,'infoF':infoF,'infoG':infoG},context_instance=RequestContext(request))

def view_bringusuarios(request):
    if request.is_ajax():
        if request.GET['data'] == 'tipo':
            try:
                tipo = request.GET['tipo']
                if tipo == 'Todos':
                    users = U.BringAll()
                else :
                    users = U.BringByTipo(tipo)
                data = [{'pk':u.user.id,'usuario':u.user.get_full_name()} for u in users]
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            except Exception,e:
                print e
                return HttpResponse('Error')
            else:
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")   
            
def view_reportestadistico(request):
    if request.method == "POST":
        
        fecha1 = request.POST['tbx_fecha1']
        fecha2 = request.POST['tbx_fecha2']
        tipousuario = request.POST['cbx_tipousuario']
        usuario = request.POST['cbx_usuario']
        departamento = request.POST['cbx_dep']
        municipio = request.POST['cbx_mun']
        centro = request.POST['cbx_centro']
       # segmentos_lista = request.POST.getlist("check_seg")
        
        sql = "SELECT * FROM Encuesta_encuesta WHERE fecha BETWEEN '" + fecha1 + "' AND '" + fecha2 + "'"
        if centro != 'Todos':
            sql = sql + " AND codigo_centro_id = " + centro
        if municipio != 'Todos':
            sql = sql + " AND codigo_municipio_id = " + municipio
        if departamento != 'Todos':
            sql = sql + " AND codigo_departamento_id = " + departamento
        if usuario != 'Todos':
            words = string.split(usuario, ' ')
            sql = sql + " AND codigo_usuario_id = (SELECT id FROM auth_user WHERE first_name = '" + words[0] + "' AND last_name = '" + words[1] + "')"
        if tipousuario != 'Todos':
            sql = sql + " AND codigo_usuario_id = (SELECT user_id FROM Administration_usuario WHERE tipo_usuario_id = (SELECT id FROM Administration_tipousuario WHERE nombre = '" + tipousuario + "'))"

        encuestas = E.objects.raw(sql)
      #  PrepareReporteEstadistico(encuestas,segmentos_lista)
        PrepareReporteEstadistico(encuestas)
    return HttpResponse('Cheque')

def PrepareReporteEstadistico(encuestas):
    #segmentos = []
    #for l in lista:
     #   if l == 'Segmento A': segmentos.append(0)
      #  if l == 'Segmento B': segmentos.append(1)
       # if l == 'Segmento C': segmentos.append(2)
        #if l == 'Segmento D': segmentos.append(3)
        #if l == 'Segmento E': segmentos.append(4)
        #if l == 'Segmento F': segmentos.append(5)
        #if l == 'Segmento G': segmentos.append(6)
    
    totala = 0
    totalb = 0
    totalc = 0
    totald = 0
    totale = 0
    totalf = 0
    totalg = 0
    
    #for e in encuestas:
     #   for s in segmentos:
     
     for e in encuestas:
         
            
        
        
            

    
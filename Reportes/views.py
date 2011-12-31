from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.utils import simplejson

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
        segmentos = lista = request.POST.getlist("check_seg")
        
        sql = "SELECT * FROM Encuesta_encuesta WHERE fecha BETWEEN " + fecha1 + " AND " + fecha2
        if centro != 'Todos':
            sql = sql + " AND codigo_centro = " + centro
        if municipio != 'Todos':
            sql = sql + " AND "
  #              if departamento == 'Todos':
   #                 if usuario == 'Todos':
    #                    if tipousuario != 'Todos':
     #                       sql = sql + 
      #                      encuestas = E.objects.filter(date__range=[fecha1, fecha2])
       #                 else:
        #                    users = U.objects.all.get_profile(tipo_usuario=tipousuario)
         #                   encuestas = E.objects.filter(date__range=[fecha1, fecha2],codigo_usuario = users.id)
          #          else:
           #             user = U.objects.get(U.get_full_name()==usuario)
            #            encuestas = E.objects.filter(date__range=[fecha1, fecha2],codigo_usuario = user.id)
             #   else:
                    
                        
                
        
        
    
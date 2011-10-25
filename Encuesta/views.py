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

from Administration.models import CentroEducativo as CE
from Administration.models import Departamento as DP
from Administration.models import Municipio as MN

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

def view_encuesta(request):
    
    if request.is_ajax():
        if request.method == 'GET':
            message = "This is an XHR GET request"
        elif request.method == 'POST':
            print "entro"
            return HttpResponse(dep)

            print request.POST
    else:

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
        return render_to_response('Encuesta.html',{'deps':deps,'centros':centros,'infoA':infoA,'infoB':infoB,'infoC':infoC,'infoD':infoD,'infoE':infoE,'infoF':infoF,'infoG':infoG,'muns':muns},context_instance=RequestContext(request))

#def view_encuesta2(request):
    
 #   infoF= SF.BringAll()
    
  #  return render_to_response('Encuesta02.html',{'infoF':infoF},context_instance=RequestContext(request))

#def send_municipios(request):
 #   if request.is_ajax():
  #      if format == 'json':
   #         mimetype = 'application/javascript'
    #    muns = serializers.serialize(format, FilterByDep(dep))
     #   return HttpResponse(muns,mimetype)
    # If you want to prevent non XHR calls
    #else:
    #    return HttpResponse(status=400)

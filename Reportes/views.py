from django.template.response import TemplateResponse
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
from Encuesta.models import EncuestaData as ED

    
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
        return PrepareReporteEstadistico(encuestas,request)

def view_reportecomparativo(request):
    if request.method == 'POST':
        fecha1 = request.POST['tbx_fecha1']
        fecha2 = request.POST['tbx_fecha2']
        centro = request.POST['cbx_centro']
        
        encuestas = E.objects.filter(codigo_centro = centro , fecha__range=(fecha1,fecha2))
        return PrepareReporteComparativo(encuestas,request)
    
def PrepareReporteComparativo(encuestas,request):
    
    idtipo = TU.objects.get(nombre = 'Director Distrital')
    iduser = U.objects.filter(tipo_usuario = idtipo.pk)
    encuestas_directordistrital = encuestas.filter(codigo_usuario__in = iduser.filter(user = iduser))
    
    llenado_dd = ""
    for e in encuestas_directordistrital:
        codigo = str(e.codigo)
        fecha = str(e.fecha_apertura)
        llenado_dd = llenado_dd + ("<tr><td><strong><a href='{%url url_encuesta " + codigo + "%}'> Encuesta " + codigo + " , fecha de creacion "+ fecha +" </a></strong></td></tr>")
       
    idtipo = TU.objects.get(nombre = 'Sociedad Civil')
    iduser = U.objects.filter(tipo_usuario = idtipo.pk)
    encuestas_sociedadcivil = encuestas.filter(codigo_usuario__in = iduser.filter(user = iduser))
    
    llenado_sc = ""
    for e in encuestas_directordistrital:
        codigo = str(e.codigo)
        fecha = str(e.fecha_apertura)
        llenado_sc = llenado_sc + ("<tr><td><strong><a href='{%url url_encuesta " + codigo + "%}'> Encuesta " + codigo + " , fecha de creacion "+fecha+" </a></strong></td></tr>")
        
    idtipo = TU.objects.get(nombre = 'Unidad de Transparencia')
    iduser = U.objects.filter(tipo_usuario = idtipo.pk)
    encuestas_unidadtransparencia = encuestas.filter(codigo_usuario__in = iduser.filter(user = iduser))
    
    llenado_ut = ""
    for e in encuestas_directordistrital:
        codigo = str(e.codigo)
        fecha = str(e.fecha_apertura)
        llenado_ut = llenado_ut + ("<tr><td><strong><a href='{%url url_encuesta " + codigo + "%}'> Encuesta " + codigo + " , fecha de creacion "+fecha+" </a></strong></td></tr>")
   
    #return TemplateResponse('Resultados_Comparativos.html',{'llenado_dd':llenado_dd})
    return render_to_response('Resultados_Comparativos.html',{'enc_dd': encuestas_directordistrital,'enc_sc': encuestas_sociedadcivil ,'enc_ut':encuestas_unidadtransparencia},context_instance=RequestContext(request))
 
def PrepareReporteEstadistico(encuestas,request):

    sega = SA.BringAll()
    segb = SB.BringAll()
    segc = SC.BringAll()
    segf = SF.BringAll()
    segg = SG.BringAll()
     
    lista = []
    for sa in sega:
        lista.append(sa.codigo)
    sum_lista = []
    for l in lista:
        sum_lista.append(0)
         
    listb = []
    for sb in segb:
        listb.append(sb.codigo)
    sum_listb = []
    for l in listb:
        sum_listb.append(0)
         
    listc = []
    for sc in segc:
        listc.append(sc.codigo)
    sum_listcSI = []
    sum_listcNO = []
    for l in listc:
        sum_listcSI.append(0)
        sum_listcNO.append(0)
         
    listf = []
    for sf in segf:
        listf.append(sf.codigo)
    sum_listf = []
    for l in listf:
        sum_listf.append(0)
         
    listg = []
    for sg in segg:
        listg.append(sg.codigo)
    sum_listgE = []
    sum_listgMB = []
    sum_listgB = []
    sum_listgR = []
    sum_listgM = []
    for l in listg:
        sum_listgE.append(0)
        sum_listgMB.append(0)
        sum_listgB.append(0)
        sum_listgR.append(0)
        sum_listgM.append(0)
     
    for e in encuestas:
        data = ED.objects.filter(encuesta=e)
        GetDataSegmentoA(data.filter(segmento = 'A'),lista,sum_lista)
        GetDataSegmentoB(data.filter(segmento = 'B'),listb,sum_listb)
        GetDataSegmentoC(data.filter(segmento = 'C'),listc,sum_listcSI,sum_listcNO)
        GetDataSegmentoF(data.filter(segmento = 'F'),listf,sum_listf)
        GetDataSegmentoG(data.filter(segmento = 'G'),listg,sum_listgE,sum_listgMB,sum_listgB,sum_listgR,sum_listgM)
    
    js = ""
        
    #Segmento A
    porcent_lista = []
    sumaa = 0
    for obj in sum_lista:
        sumaa = sumaa + obj
    for obj in sum_lista:
        element = (float(obj) / float(sumaa)) * 100.0
        porcent_lista.append(element)
         
    js = js + ("chartA = new Highcharts.Chart({"                                                    +
                    "chart: {"                                                                      +
                    "renderTo: 'SegmentoA',"                                                           +
                    "    plotBackgroundColor: null,"                                                +
                    "    plotBorderWidth: null,"                                                    +
                    "    plotShadow: false"                                                         +    
                    "        },"                                                                    +
                    "title:{"                                                                       +
                    "    text: 'Instalacion y Ubicacion del Mural'"                                 +
                    "    },"                                                                        +
                    "tooltip: {"                                                                    +
                    "    formatter: function() {"                                                   +
                    "        return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';"       +
                    "    }"                                                                         +
                    "},"                                                                            +
                    "plotOptions: {"                                                                +
                    "    pie: {"                                                                    +
                    "        allowPointSelect: true,"                                               +
                    "        cursor: 'pointer',"                                                    +
                    "        dataLabels: {"                                                         +
                    "            enabled: true,"                                                    +
                    "            color: '#000000',"                                                 +
                    "            connectorColor: '#000000',"                                        +
                    "            formatter: function() {"                                           +
                    "               return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';"+
                    "            }"                                                                 +
                    "        }"                                                                     +
                    "    }"                                                                         +
                    "},"                                                                            +
                    "series: [{"                                                                    +                                                
                    "    type: 'pie',"                                                              +    
                    "    name: 'Segmento A',"                                                       +    
                    "    data: ["                                                                   
                    )

    index = 0;
    for item in porcent_lista:
        if index != 0:
            js = js + ","
        js = js + ("['" + unicode(sega[index].descripcion) +"' , "+ unicode(item) + "]")
        index = index + 1

    js = js + (                     "]" +
                                "}]"+
                            "});")
    
    #Segmento B
    porcent_listb = []
    sumab = 0
    for obj in sum_listb:
        sumab = sumab + obj
    for obj in sum_listb:
        element = (float(obj) / float(sumab)) * 100.0
        print element
        porcent_listb.append(element)
         
    js = js + ("chartB = new Highcharts.Chart({"                                                    +
                    "chart: {"                                                                      +
                    "renderTo: 'SegmentoB',"                                                           +
                    "    plotBackgroundColor: null,"                                                +
                    "    plotBorderWidth: null,"                                                    +
                    "    plotShadow: false"                                                         +    
                    "        },"                                                                    +
                    "title:{"                                                                       +
                    "    text: 'Informacion Obligatoria Publicada en Mural'"                        +
                    "    },"                                                                        +
                    "tooltip: {"                                                                    +
                    "    formatter: function() {"                                                   +
                    "        return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';"       +
                    "    }"                                                                         +
                    "},"                                                                            +
                    "plotOptions: {"                                                                +
                    "    pie: {"                                                                    +
                    "        allowPointSelect: true,"                                               +
                    "        cursor: 'pointer',"                                                    +
                    "        dataLabels: {"                                                         +
                    "            enabled: true,"                                                    +
                    "            color: '#000000',"                                                 +
                    "            connectorColor: '#000000',"                                        +
                    "            formatter: function() {"                                           +
                    "               return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';"+
                    "            }"                                                                 +
                    "        }"                                                                     +
                    "    }"                                                                         +
                    "},"                                                                            +
                    "series: [{"                                                                    +                                                
                    "    type: 'pie',"                                                              +    
                    "    name: 'Segmento B',"                                                       +    
                    "    data: ["                                                                   
                    )


    index = 0;
    for item in porcent_listb:
        if index != 0:
            js = js + ","
        js = js + ("['" + unicode(segb[index].descripcion) +"' , "+ unicode(item) + "]")
        index = index + 1
    js = js + (                     "]" +
                                "}]"+
                            "});")

    #Segmento C
    sumacSI = 0
    sumacNO = 0
    for obj in sum_listcSI:
        sumacSI = sumacSI + obj
    for obj in sum_listcNO:
        sumacNO = sumacNO + obj
         
    js = js + ("chartC = new Highcharts.Chart({"                                                    +
                    "chart: {"                                                                      +
                        "renderTo: 'SegmentoC',"                                                           +
                        "defaultSeriesType: 'bar'"                                                      +
                    "        },"                                                                    +
                    "title:{"                                                                       +
                    "    text: 'Orden de la Informacion'"                        +
                    "    },"                                                                        +

                "xAxis: {"+
                "categories: [")
    
    index = 0
    for item in segc:
        if index !=0:
            js = js + ","
        js = js + "'" + item.descripcion +"'"
        index = index + 1
        
    js = js + ("],"+
         "title: {"+
            "text: null"+
         "}"+
      "},"+
                    "  yAxis: {"+
                     "    min: 0,"+
                      "   title: {"+
                       "     text: 'Resultados',"+
                        "    align: 'high'"+
                         "}"+
                      "},"+
                    "tooltip: {"                                                                    +
                    "formatter: function() {"+
                    "    return ''+"+
                    "        this.series.name +': '+ this.y;"+
                    " }"                                     +
                    "},"                                                                            +
                    "plotOptions: {"                                                                +
                     "bar: {"+
                      "  dataLabels: {"+
                       "    enabled: true"+
                        "}}"+
                     "},"                                                                            +
                     " legend: {"+
                     "    layout: 'vertical',"+
                     "    align: 'right',"+
                     "    verticalAlign: 'top',"+
                     "    x: -100,"+
                     "    y: 100,"+
                     "    floating: true,"+
                     "    borderWidth: 1,"+
                    "backgroundColor: '#FFFFFF',"+
                     "    shadow: true"+
                      "},"+
                      "credits: {"+
                         "enabled: false"+
                      "},"+
                    "series: [{"+
                        "name:'SI',"+
                        "data:["                                                                                                                                                                         
                    )
    index = 0;
    for item in listc:
        if index != 0:
            js = js + ","
        js = js + (unicode(sum_listcSI[index]))
        index = index + 1
    js = js + ("]},{"+
                        "name : 'NO',"+
                        "data:["  )
    index = 0;
    for item in listc:
        if index != 0:
            js = js + ","
        js = js + (unicode(sum_listcNO[index]))
        index = index + 1
    js = js + ("]}]"+
 "});")
    
    #Segmento F
    porcent_listf = []
    sumaf = 0
    for obj in sum_listf:
        sumaf = sumaf + obj
    for obj in sum_listf:
        element = (float(obj) / float(sumaf)) * 100.0
        porcent_listf.append(element)
         
    js = js + ("chartF = new Highcharts.Chart({"                                                    +
                    "chart: {"                                                                      +
                    "renderTo: 'SegmentoF',"                                                           +
                    "    plotBackgroundColor: null,"                                                +
                    "    plotBorderWidth: null,"                                                    +
                    "    plotShadow: false"                                                         +    
                    "        },"                                                                    +
                    "title:{"                                                                       +
                    "    text: 'Hallazgos e Irregularidades en Matricula Gratis'"                        +
                    "    },"                                                                        +
                    "tooltip: {"                                                                    +
                    "    formatter: function() {"                                                   +
                    "        return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';"       +
                    "    }"                                                                         +
                    "},"                                                                            +
                    "plotOptions: {"                                                                +
                    "    pie: {"                                                                    +
                    "        allowPointSelect: true,"                                               +
                    "        cursor: 'pointer',"                                                    +
                    "        dataLabels: {"                                                         +
                    "            enabled: true,"                                                    +
                    "            color: '#000000',"                                                 +
                    "            connectorColor: '#000000',"                                        +
                    "            formatter: function() {"                                           +
                    "               return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';"+
                    "            }"                                                                 +
                    "        }"                                                                     +
                    "    }"                                                                         +
                    "},"                                                                            +
                    "series: [{"                                                                    +                                                
                    "    type: 'pie',"                                                              +    
                    "    name: 'Segmento F',"                                                       +    
                    "    data: ["                                                                   
                    )


    index = 0;
    for item in porcent_listf:
        if index != 0:
            js = js + ","
        js = js + ("['" + unicode(segf[index].descripcion) +"' , "+ unicode(item) + "]")
        index = index + 1
    js = js + (                     "]" +
                                "}]"+
                            "});")
    
    #SegmentoG

    sumagE = 0
    sumagMB = 0
    sumagB = 0
    sumagR = 0
    sumagM = 0
    for obj in sum_listgE:
        sumagE = sumagE + obj
    for obj in sum_listgMB:
        sumagMB = sumagMB + obj
    for obj in sum_listgB:
        sumagB = sumagB + obj
    for obj in sum_listgR:
        sumagR = sumagR + obj
    for obj in sum_listgM:
        sumagM = sumagM + obj

         
    js = js + ("chartC = new Highcharts.Chart({"                                                    +
                    "chart: {"                                                                      +
                        "renderTo: 'SegmentoG',"                                                           +
                        "defaultSeriesType: 'bar'"                                                      +
                    "        },"                                                                    +
                    "title:{"                                                                       +
                    "    text: 'Creatividad'"                        +
                    "    },"                                                                        +

                "xAxis: {"+
                "categories: [")
    
    index = 0
    for item in segc:
        if index !=0:
            js = js + ","
        js = js + "'" + item.descripcion +"'"
        index = index + 1
        
    js = js + ("],"+
         "title: {"+
            "text: null"+
         "}"+
      "},"+
                    "  yAxis: {"+
                     "    min: 0,"+
                      "   title: {"+
                       "     text: 'Resultados',"+
                        "    align: 'high'"+
                         "}"+
                      "},"+
                    "tooltip: {"                                                                    +
                    "formatter: function() {"+
                    "    return ''+"+
                    "        this.series.name +': '+ this.y;"+
                    " }"                                     +
                    "},"                                                                            +
                    "plotOptions: {"                                                                +
                     "bar: {"+
                      "  dataLabels: {"+
                       "    enabled: true"+
                        "}}"+
                     "},"                                                                            +
                     " legend: {"+
                     "    layout: 'vertical',"+
                     "    align: 'right',"+
                     "    verticalAlign: 'top',"+
                     "    x: -100,"+
                     "    y: 100,"+
                     "    floating: true,"+
                     "    borderWidth: 1,"+
                    "backgroundColor: '#FFFFFF',"+
                     "    shadow: true"+
                      "},"+
                      "credits: {"+
                         "enabled: false"+
                      "},"+
                    "series: [{"+
                        "name:'Excelente',"+
                        "data:["                                                                                                                                                                         
                    )
    index = 0;
    for item in listc:
        if index != 0:
            js = js + ","
        js = js + (unicode(sum_listgE[index]))
        index = index + 1
    js = js + ("]},{"+
                        "name : 'Muy Bueno',"+
                        "data:["  )
    index = 0;
    for item in listc:
        if index != 0:
            js = js + ","
        js = js + (unicode(sum_listgMB[index]))
        index = index + 1
    js = js + ("]},{"+
                        "name : 'Bueno',"+
                        "data:["  )
    index = 0;
    for item in listc:
        if index != 0:
            js = js + ","
        js = js + (unicode(sum_listgB[index]))
        index = index + 1
    js = js + ("]},{"+
                        "name : 'Regular',"+
                        "data:["  )
    index = 0;
    for item in listc:
        if index != 0:
            js = js + ","
        js = js + (unicode(sum_listgR[index]))
        index = index + 1
    js = js + ("]},{"+
                        "name : 'Malo',"+
                        "data:["  )
    index = 0;
    for item in listc:
        if index != 0:
            js = js + ","
        js = js + (unicode(sum_listgM[index]))
        index = index + 1
    js = js + ("]}]"+
 "});")

    return render_to_response('Resultados_Estadisticos.html',{'js':js},context_instance=RequestContext(request))
 
    

def GetDataSegmentoA(datos,items,sum_lista):
     for d in datos:
         code = d.codigo_item
         if code in items:
             index = items.index(code)
             sum = sum_lista[index] + 1
             del sum_lista[index]
             sum_lista.insert(index,sum)
def GetDataSegmentoB(datos,items,sum_listb):

     for d in datos:
         code = d.codigo_item
         if code in items:
             index = items.index(code)
             sum = sum_listb[index] + 1
             del sum_listb[index]
             sum_listb.insert(index,sum)
def GetDataSegmentoC(datos,items,sum_listcSI,sum_listcNO):

     for d in datos:
         code = d.codigo_item
         if d.valor_item == 'SI':
             index = items.index(code)
             sum = sum_listcSI[index] + 1
             del sum_listcSI[index]
             sum_listcSI.insert(index,sum)
         else:
             index = items.index(code)
             sum = sum_listcNO[index] + 1
             del sum_listcNO[index]
             sum_listcNO.insert(index,sum)

def GetDataSegmentoF(datos,items,sum_listf):

     for d in datos:
         code = d.codigo_item
         if code in items:
             index = items.index(code)
             sum = sum_listf[index] + 1
             del sum_listf[index]
             sum_listf.insert(index,sum)
def GetDataSegmentoG(datos,items,sum_listgE,sum_listgMB,sum_listgB,sum_listgR,sum_listgM):

     for d in datos:
         code = d.codigo_item
         if d.valor_item == 'Excelente':
             index = items.index(code)
             sum = sum_listgE[index] + 1
             del sum_listgE[index]
             sum_listgE.insert(index,sum)
         if d.valor_item == 'Muy Bueno':
             index = items.index(code)
             sum = sum_listgMB[index] + 1
             del sum_listgMB[index]
             sum_listgMB.insert(index,sum)
         if d.valor_item == 'Bueno':
             index = items.index(code)
             sum = sum_listgB[index] + 1
             del sum_listgB[index]
             sum_listgB.insert(index,sum)
         if d.valor_item == 'Regular':
             index = items.index(code)
             sum = sum_listgR[index] + 1
             del sum_listgR[index]
             sum_listgR.insert(index,sum)
         if d.valor_item == 'Malo':
             index = items.index(code)
             sum = sum_listgM[index] + 1
             del sum_listgM[index]
             sum_listgM.insert(index,sum)
     
        
            

    
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
import string
from Administration.models import TipoUsuario as TU
from Administration.models import Rol as RU
from Administration.models import CentroEducativo 
from Encuesta.models import EncuestaTemp as ET
from Encuesta.models import EncuestaTempData as ETD
from Encuesta.models import Encuesta as E
from Encuesta.models import EncuestaData as ED
from django.contrib.auth.models import User 


def view_login(request):
    try:
        username = ''
        password = ''
		
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
    
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_anonymous():
                    return render_to_response('Login.html',{'username': username},context_instance=RequestContext(request))
                else:
                    if user.is_active:
                        login(request, user)
                        return PrepareContent(user,request)
                    else:
                        return render_to_response('Login.html',{'username': username},context_instance=RequestContext(request))
            else:
                return render_to_response('Login.html',{'username': username,'err':'Error de ingreso, favor revise sus datos'},context_instance=RequestContext(request))
        else: return render_to_response('Login.html',{'username': username},context_instance=RequestContext(request))
    except Exception,e:
        return HttpResponse(e)

def view_logout(request):
    logout(request)
    return render_to_response('Login.html',context_instance=RequestContext(request))
    
def view_home(request):
    try:
        if request.user.is_active:
            return PrepareContent(request.user,request)
            
        else:
            return render_to_response('Login.html',context_instance=RequestContext(request))
    except Exception,e:
        return HttpResponse(e)

def PrepareContent(user,request):
    try:
        usuario = user.get_full_name()
        #usuario = user.first_name
        id_usuario = user.id
        #rol_usuario = RU.objects.get(codigo = user.get_profile().rol.codigo)
        rol_usuario = RU.objects.get(codigo = user.rol.codigo)
        encuestas_pendientes = ET.objects.filter(codigo_usuario = user)
        encuestas_publicadas = E.objects.filter(codigo_usuario=user)

        try:
            tipo = request.POST['tipo_save']
        except:
            tipo = ""
            
        try:
            despub = request.POST['msg']
        except Exception,e:
            despub=""
            
        return render_to_response('Home.html',{'usuario':usuario,'rol_usuario':rol_usuario.nombre,'encuestas':encuestas_pendientes,'publicadas':encuestas_publicadas,'mssg':tipo,'despub':despub},context_instance=RequestContext(request))
    except Exception,e:
        return HttpResponse(e)


def view_adminusuarios(request):

    return redirect('/admin/Administration/usuario/')
def view_adminsegmentos(request):
    try:
        return render_to_response('MenuSegmentos.html',context_instance=RequestContext(request))
    except Exception,e:
		return HttpResponse(e)
	
def view_adminencuestas(request):
    try:
        usuarios = User.objects.all
        tipos = TU.BringAll()
        return render_to_response('Admin_Encuestas.html',{'usuarios':usuarios,'tipos':tipos},context_instance=RequestContext(request))
    except Exception,e:
        return HttpResponse(e)
    
def view_bringencuestas(request):
    if request.is_ajax():
        if request.GET['data'] == 'usuario':
            try:
                pk = request.GET['usuario']
                #words = string.split(usuario_name, ' ')
                user = User.objects.get(pk=pk).username
                encuestas = E.objects.filter(codigo_usuario=pk)
                
                data = [{'user':user,'pk':e.codigo,'fecha':str(e.fecha),'fecha_cre':str(e.fecha_apertura),'centro':e.codigo_centro.nombre} for e in encuestas]
            
                #data = [{'pk':e.codigo} for e in encuestas]
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            except Exception,e:
                return HttpResponse(e)
            #else:
                #return HttpResponse(simplejson.dumps(data), mimetype="application/json")   

		
def view_despubencuestas(request,encuesta):
    try:
        encuesta = E.objects.get(pk = encuesta)
        datos = ED.objects.filter(encuesta = encuesta)
        
        p = ET(fecha = encuesta.fecha, codigo_usuario = encuesta.codigo_usuario,codigo_centro = encuesta.codigo_centro, zona = encuesta.zona, tel = encuesta.tel, fecha_apertura = encuesta.fecha_apertura)
        p.save()
        
        for d in datos:
            p2 = ETD(encuesta = p,codigo_item = d.codigo_item,tipo_valor = d.tipo_valor,valor_item = d.valor_item, segmento = d.segmento)
            p2.save()
        
        encuesta.delete()
        datos.delete()
        
        return PrepareContent(request.user,request)
    except Exception,e:
        return HttpResponse(e)
    
        
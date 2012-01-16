
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
import string
from Administration.models import TipoUsuario as TU
from Administration.models import Rol as RU
from Encuesta.models import EncuestaTemp as ET
from Encuesta.models import EncuestaTempData as ETD
from Encuesta.models import Encuesta as E
from Encuesta.models import EncuestaData as ED
from django.contrib.auth.models import User 

def view_home(request):
    
    print request.user
    if request.user.is_active:
        print "activo"  
        return PrepareContent(request.user,request)
        
    else:
        print "inactivo"
        return redirect('/admin/')

def view_autenticar(request):

    if request.method=='POST':
        #un = request.POST['user_tbx']
        #pd = request.POST['pass_tbx']
        un = request.POST['username']
        pd = request.POST['password']
        #un = self.cleaned_data.get('username')
        #pd = self.cleaned_data.get('password')
        user = authenticate(username = un,password = pd)
        if user is not None:
            try:
                if user.is_active:
                    login(request, user)
                    return PrepareContent(user,request)
            except :
                
                return redirect('/admin/')
        else :
            return HttpResponse("usuario no existe")
    #return render_to_response('Login.html',context_instance=RequestContext(request))
    #return render_to_response('Home.html',context_instance=RequestContext(request))

def PrepareContent(user,request):
    
    usuario = user.get_full_name()
    id_usuario = user.id
    rol_usuario = RU.objects.get(codigo = user.get_profile().rol.codigo)
    encuestas_pendientes = ET.objects.filter(codigo_usuario = user)
    encuestas_publicadas = E.objects.filter(codigo_usuario=user)
    
    try:
        tipo = request.POST['tipo_save']
    except:
        tipo = ""
        

    return render_to_response('Home.html',{'usuario':usuario,'rol_usuario':rol_usuario.nombre,'encuestas':encuestas_pendientes,'publicadas':encuestas_publicadas,'mssg':tipo},context_instance=RequestContext(request))
    
def view_adminusuarios(request):

    return redirect('/admin/Administration/usuario/')
def view_adminsegmentos(request):
    
    return redirect('/admin/Encuesta/')
def view_adminencuestas(request):

    usuarios = User.objects.all
    tipos = TU.BringAll()
    return render_to_response('Admin_Encuestas.html',{'usuarios':usuarios,'tipos':tipos},context_instance=RequestContext(request))
def view_bringencuestas(request):
    if request.is_ajax():
        if request.GET['data'] == 'usuario':
            try:
                usuario_name = request.GET['usuario']
                words = string.split(usuario_name, ' ')
                user = User.objects.get(first_name = words[0],last_name = words[1])
                encuestas = E.objects.filter(codigo_usuario = user)
                data = [{'pk':e.codigo} for e in encuestas]
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            except Exception,e:
                print e
                return HttpResponse('Error')
            else:
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")   

def view_despubencuestas(request,encuesta):
    
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
    
        
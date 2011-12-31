from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from Administration.models import TipoUsuario as TU
from Administration.models import Rol as RU
from Encuesta.models import EncuestaTemp as ET
from Encuesta.models import Encuesta as E

def view_home(request):
    
    print request.user
    if request.user.is_active:
        print "activo"  
        return PrepareContent(request.user,request)
        
    else:
        print "inactivo"
        return redirect('/admin/')

        
   # else:
        #return render_to_response('Login.html',context_instance=RequestContext(request))
        #return render_to_response('admin/login.html',context_instance=RequestContext(request))
        #return redirect('url_autenticar')
    #return HttpResponseRedirect('transparencia/home/autenticar')
    #return render_to_response('Login.html',context_instance=RequestContext(request))
   # return HttpResponse("Home")

#@login_required(login_url='/admin/')
def view_autenticar(request):
    print 'autenticando...'
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

    return redirect('/admin/Administration/usuario/')
#def view_adminreportes(request):

   # return redirect('/admin/Administration/usuario/')
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson
from django.core import serializers

from Transparencia.Administration.forms import UsuarioForm,UsuarioModForm
from Transparencia.Administration.models import *
from Transparencia.Encuesta.models import *

from Transparencia.Encuesta.forms import SAForm as SAF
from Transparencia.Encuesta.forms import SBForm as SBF
from Transparencia.Encuesta.forms import SCForm as SCF
from Transparencia.Encuesta.forms import SDForm as SDF
from Transparencia.Encuesta.forms import SEForm as SEF
from Transparencia.Encuesta.forms import SFForm as SFF
from Transparencia.Encuesta.forms import SGForm as SGF

from Administration.models import Rol as RU
from Encuesta.models import EncuestaTemp as ET
from Encuesta.models import Encuesta as E

from Transparencia.views import PrepareContent
from django.core.urlresolvers import reverse
import random,string

def view_menuusuarios(request):
    try:
        #if request.method == 'POST':
        form = UsuarioForm(request.POST or None)
        tipos = TipoUsuario.BringAll()
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                form = UsuarioForm(None)

                
                return render_to_response('MenuUsuarios.html',{'form': form,'tipos':tipos,'mssg':"user_add"},context_instance=RequestContext(request))
            else:
                
                return render_to_response('MenuUsuarios.html',{'form': form,'tipos':tipos,'mssg':"user_error"},context_instance=RequestContext(request))
        else:
            return render_to_response('MenuUsuarios.html',{'form': form,'tipos':tipos},context_instance=RequestContext(request))
            
    except Exception,e:
        return HttpResponse(e)

def view_gestionsegmentos(request,segmento):
    if segmento == 'A':
        try:
            form = SAF(request.POST or None)
            if form.is_valid():
                f = form.save()
                f.save()
                form = SAF(None)
            return render_to_response('MenuSegmentos.html',{'form': form},context_instance=RequestContext(request))
        except Exception,e:
            return HttpResponse(e)

def view_bringsegmento(request):
    if request.is_ajax():
        if request.GET['data'] == 'traer':
            try:
                segmento = request.GET['segmento']
                if segmento != '':
                    if segmento == 'a':
                        segs = SegmentoA.objects.all()
                    elif segmento == 'b':
                        segs = SegmentoB.objects.all()
                    elif segmento == 'c':
                        segs = SegmentoC.objects.all()
                    elif segmento == 'd':
                        segs = SegmentoD.objects.all()
                    elif segmento == 'e':
                        segs = SegmentoE.objects.all()
                    elif segmento == 'f':
                        segs = SegmentoF.objects.all()
                    elif segmento == 'g':
                        segs = SegmentoG.objects.all()

                ret = [{'pk':s.pk,'descripcion':s.descripcion} for s in segs]
                return HttpResponse(simplejson.dumps(ret), mimetype="application/json")
            except Exception,e:
                return HttpResponse(e)
            else:
                return HttpResponse(simplejson.dumps(ret), mimetype="application/json")
        else:
            if request.GET['data'] == 'modificar':
                try:
                    segmento = request.GET['segmento']
                    id_seg= request.GET['id_seg']

                    if segmento=='a':
                        form = SAF(instance = SegmentoA.objects.get(pk=id_seg))

                        html = render_to_string( 'userform.html', { 'form': form } )
                        res = {'html': html}
                        return HttpResponse( simplejson.dumps(res),'application/json' )
                    elif segmento=='b':
                        form = SBF(instance = SegmentoB.objects.get(pk=id_seg))

                        html = render_to_string( 'userform.html', { 'form': form } )
                        res = {'html': html}
                        return HttpResponse( simplejson.dumps(res),'application/json' )
                    elif segmento=='c':
                        form = SCF(instance = SegmentoC.objects.get(pk=id_seg))

                        html = render_to_string( 'userform.html', { 'form': form } )
                        res = {'html': html}
                        return HttpResponse( simplejson.dumps(res),'application/json' )
                    elif segmento=='d':
                        form = SDF(instance = SegmentoD.objects.get(pk=id_seg))

                        html = render_to_string( 'userform.html', { 'form': form } )
                        res = {'html': html}
                        return HttpResponse( simplejson.dumps(res),'application/json' )
                    elif segmento=='e':
                        form = SEF(instance = SegmentoE.objects.get(pk=id_seg))

                        html = render_to_string( 'userform.html', { 'form': form } )
                        res = {'html': html}
                        return HttpResponse( simplejson.dumps(res),'application/json' )
                    elif segmento=='f':
                        form = SFF(instance = SegmentoF.objects.get(pk=id_seg))

                        html = render_to_string( 'userform.html', { 'form': form } )
                        res = {'html': html}
                        return HttpResponse( simplejson.dumps(res),'application/json' )
                    elif segmento=='g':
                        form = SGF(instance = SegmentoG.objects.get(pk=id_seg))

                        html = render_to_string( 'userform.html', { 'form': form } )
                        res = {'html': html}
                        return HttpResponse( simplejson.dumps(res),'application/json' )

                except Exception, e:
                    return HttpResponse(e)
                #else:
                    #return HttpResponse(simplejson.dumps(form), mimetype="application/json")
                    
                    
def view_bringusers(request):
    if request.is_ajax():
        if request.GET['data'] == 'users':
            try:
                nuser = request.GET['username']
                tipo = request.GET['tipo']
                if nuser != '':
                    if tipo == 'Todos':
                        users=Usuario.BringByTipo_Username(None,nuser)
                    else:
                        id_tipo = TipoUsuario.objects.get(codigo=tipo)
                        users=Usuario.BringByTipo_Username(id_tipo,nuser)
                else:
                    if tipo == 'Todos':
                        users=Usuario.BringAll()
                    else:
                        id_tipo = TipoUsuario.objects.get(codigo=tipo)
                        users=Usuario.BringByTipo_Username(id_tipo,None)

                ret = [{'pk':u.pk,'name':u.get_full_name(),'usuario':u.username,'tipo':u.tipo_usuario.nombre, 'url':reverse('url_deleteuser', args=[u.pk]), 'url_reset':reverse('url_pwdreset', args=[u.pk]) } for u in users]
                return HttpResponse(simplejson.dumps(ret), mimetype="application/json")
            except Exception,e:
                return HttpResponse(e)
            else:
                return HttpResponse(simplejson.dumps(ret), mimetype="application/json")
        else:
            if request.GET['data'] == 'modificar':
                try:
                    id_user= request.GET['id_user']
                    form = UsuarioModForm(instance = Usuario.objects.get(pk=id_user))

                    html = render_to_string( 'userform.html', { 'form': form } )
                    res = {'html': html}
                    return HttpResponse( simplejson.dumps(res),'application/json' )
                except Exception,e:
                    return HttpResponse(e)
            '''else:
                    id = request.GET['id_user']
                    if id != '':
                        user = Usuario.objects.get(pk=id)
                        user.delete()

                        form_original = UsuarioForm()
                        tipos = TipoUsuario.BringAll()
                        return render_to_response('MenuUsuarios.html',{'form':form_original,'mssg': "user_del",'tipos':tipos},context_instance=RequestContext(request))'''

def view_deleteuser(request,pk):
    user = Usuario.objects.get(pk=pk)
    user.is_active = False
    user.save()
    
    #user.delete()

    form_original = UsuarioForm()
    tipos = TipoUsuario.BringAll()
    
    return render_to_response('MenuUsuarios.html',{'form':form_original,'mssg': "user_del",'tipos':tipos},context_instance=RequestContext(request))

def view_pwdreset(request,pk):
    
    usuario= User.objects.get(pk=pk)
    pwd=''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(12))
    
    usuario.set_password(pwd)
    usuario.save()
    
    
    form_original = UsuarioForm()
    tipos = TipoUsuario.BringAll()
    
    return render_to_response('MenuUsuarios.html',{'form':form_original,'mssg': "user_reset",'tipos':tipos,'pwd':pwd},context_instance=RequestContext(request))
    
def view_modificarusuario(request,tipo):
    if tipo=="datos":
        try:
            form_original = UsuarioForm()
            tipos = TipoUsuario.BringAll()

            pk = request.POST['pk']
            form = UsuarioModForm(request.POST,instance = Usuario.objects.get(pk=pk))

            if form.is_valid():
                form.save()

                return render_to_response('MenuUsuarios.html',{'form':form_original,'mssg': "user_mod",'tipos':tipos},context_instance=RequestContext(request))
            else:
                return render_to_response('MenuUsuarios.html',{'form':form_original,'form_update': form,'tipos':tipos,'mssg': "user_error",},context_instance=RequestContext(request))

        except Exception,e:
            return HttpResponse(e)
            
    else:
        try:
            errores,ret_data = {},{}
            user=request.user
            contrasena = request.POST.get('name_conactual','')
            contrasena01 = request.POST.get('name_connueva01','')
            contrasena02 = request.POST.get('name_connueva02','')

            if contrasena == '':
                errores['conactual']=u'Ingrese la contrasena actual'
            if contrasena01 == '':
                errores['connueva01']=u'Ingrese la contrasena nueva'
            if contrasena02 == '':
                errores['connueva02']=u'Confirme su contrasena'
              
            if not errores:
                if user.check_password(contrasena):
                    if contrasena01 == contrasena02:
                        user.set_password(contrasena01)
                        user.save()                      
                    else:
                        errores['connueva01']=u'Las contrasenas no concuerdan'
                else:
                    errores['conactual'] = u'La contrasena no es v\E1lida'

            if not errores:
                return PrepareContent2(user,request,'pssw_modif',None,None)
                #return render_to_response('Home.html',{'mssg':u'pssw_modif'},context_instance=RequestContext(request))
            else:
                return PrepareContent2(user,request,'pssw_error',ret_data,errores)
                #return render_to_response('Home.html',{'tipo':tipo,'ret_data':ret_data,'errores':errores},context_instance=RequestContext(request))
            
        except Exception,e:
            return HttpResponse(e)

def PrepareContent2(user,request,mssg,ret_data,errores):
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
            
        if errores == None:
            return render_to_response('Home.html',{'usuario':usuario,'rol_usuario':rol_usuario.nombre,'encuestas':encuestas_pendientes,'publicadas':encuestas_publicadas,'mssg':mssg},context_instance=RequestContext(request))
            
        else:
            return render_to_response('Home.html',{'usuario':usuario,'rol_usuario':rol_usuario.nombre,'encuestas':encuestas_pendientes,'publicadas':encuestas_publicadas,'mssg':mssg,'ret_data':ret_data,'errores':errores},context_instance=RequestContext(request))
    except Exception,e:
        return HttpResponse(e)
        
def view_modificarsegmento(request):
    try:
        pk = request.POST['pk']
        segmento = request.POST['seg_pk']

        if segmento=='a':
            form = SAF(request.POST,instance = SegmentoA.objects.get(pk=pk))

        elif segmento=='b':
            form = SAB(request.POST,instance = SegmentoB.objects.get(pk=pk))

        elif segmento=='c':
            form = SCF(request.POST,instance = SegmentoC.objects.get(pk=pk))

        elif segmento=='d':
            form = SDF(request.POST,instance = SegmentoD.objects.get(pk=pk))

        elif segmento=='e':
            form = SEF(request.POST,instance = SegmentoE.objects.get(pk=pk))

        elif segmento=='f':
            form = SFF(request.POST,instance = SegmentoF.objects.get(pk=pk))

        elif segmento=='g':
            form = SGF(request.POST,instance = SegmentoG.objects.get(pk=pk))

        if form.is_valid():
            form.save()

            return render_to_response('MenuSegmentos.html',{'mssg': "seg_mod"},context_instance=RequestContext(request))
        else:

            return render_to_response('MenuSegmentos.html',context_instance=RequestContext(request))

    except Exception,e:
        return HttpResponse(e)


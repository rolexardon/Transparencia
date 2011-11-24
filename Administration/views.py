from Administration.forms import UserForm as UF, TiposForm as TF, RolesForm as RF, ProfileUserForm as PUF
from Administration.models import TipoUsuario as TU, Rol,Usuario as US
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User 

# Create your views here.
def view_usuarios(request):

    form = UF()
    form2 = PUF()
    usuarios = US.BringAll()
    return render_to_response('Usuarios.html', {'form': form,'form2':form2,'usuarios':usuarios},context_instance=RequestContext(request))
    
def view_tipos(request):
    form = TF()
    tipos = TU.BringAll()
    
    return render_to_response('TiposUsuarios.html', {'form': form, 'tipos' : tipos},context_instance=RequestContext(request))

def view_roles(request):
    form = RF()
    roles =  Rol.BringAll()
    
    return render_to_response('Roles.html', {'form': form,'roles':roles},context_instance=RequestContext(request))

def view_saveusuario(request):
    
    if request.method == 'POST':
        form = UF(request.POST)
        form2=PUF(request.POST)
        if form.is_valid() and form2.is_valid():
            user=form.save(commit = False)
            pdw = form.cleaned_data['password']
            eml = form.cleaned_data['email']
            user.set_password(pdw)
            user.email = eml
            user.save()  
            profile = form2.save(commit = False)
            profile.user = user
            profile.save()
            return HttpResponse('se guardo')
        else:
            form = UF()
            form2=PUF()
            return render_to_response('TiposUsuarios.html', { 'form': form,'form2':form2 },context_instance=RequestContext(request))
    return HttpResponse('hola')
def view_savetipo(request):

    if request.method == 'POST':
        form = TF(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('se guardo')
        else:
            form = TF()
            return render_to_response('TiposUsuarios.html', { 'form': form, },context_instance=RequestContext(request))
    
def view_saverol(request):
    
    if request.method == 'POST':
        form = RF(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('se guardo')
        else:
            form = RF()
            return render_to_response('TiposUsuarios.html', { 'form': form, },context_instance=RequestContext(request))
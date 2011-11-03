from Administration.forms import UserForm as UF, TiposForm as TF, RolesForm as RF
from Administration.models import TipoUsuario as TU, Rol,Usuario as US
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext


# Create your views here.
def view_usuarios(request):
    form = UF()
    usuarios = US.BringAll()
    
    return render_to_response('Usuarios.html', {'form': form,'usuarios':usuarios},context_instance=RequestContext(request))
    
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
        if form.is_valid():
            form.save()
            return HttpResponse('se guardo')
        else:
            form = UF()
            return render_to_response('TiposUsuarios.html', { 'form': form, },context_instance=RequestContext(request))
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
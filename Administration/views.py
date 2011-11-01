from Administration.forms import UserForm as UF
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response,redirect,get_object_or_404
# Create your views here.
def view_usuarios(request):
    form = UF() # An unbound form
    return render_to_response('Usuarios.html', {
        'form': form,
    })
def view_saveusuario(request):
    
    return HttpResponse('hola')
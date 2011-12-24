from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse

from django.contrib.auth.models import User 
from Administration.models import TipoUsuario as TU

def view_reporte(request):
    
    usuarios = User.objects.all
    tipos = TU.BringAll()
    
    return render_to_response('Reportes.html',{'usuarios':usuarios,'tipos':tipos},context_instance=RequestContext(request))
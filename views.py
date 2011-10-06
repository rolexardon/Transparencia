from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse


def view_home(request):
    
    state=False
    if state:
        return redirect('url_home')
    else:
        return render_to_response('Login.html',context_instance=RequestContext(request))
        #return redirect('url_autenticar')
    #return HttpResponseRedirect('transparencia/home/autenticar')
    #return render_to_response('Login.html',context_instance=RequestContext(request))
    return HttpResponse("Home")

def view_autenticar(request):
    
    if request.method=='POST':
        username = request.POST.get('user_tbx','')
        password = request.POST.get('pass_tbx','')
        #return redirect('url_home')
        return render_to_response('Home.html',context_instance=RequestContext(request))
    #return render_to_response('Login.html',context_instance=RequestContext(request))
    return render_to_response('Home.html',context_instance=RequestContext(request))



    
    
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import authenticate, login



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
        
        un = request.POST['user_tbx']
        pd = request.POST['pass_tbx']
        user = authenticate(username = un,password = pd)
        if user is not None:
            if user.is_active:
                login(request, user)
                PrepareContent(user,request)
        else :
            return HttpResponse("nada")
    #return render_to_response('Login.html',context_instance=RequestContext(request))
    return render_to_response('Home.html',context_instance=RequestContext(request))

def PrepareContent(user,request):
    
    usuario = user.get_full_name()
    return render_to_response('Home.html',{'usuario':usuario},context_instance=RequestContext(request))
    
    
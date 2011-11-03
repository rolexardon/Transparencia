from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Administration.views',
                       
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^usuarios$','view_usuarios',name = 'url_usuarios'),
    url(r'^usuarios/tipos$','view_tipos',name = 'url_tipos'),
    url(r'^usuarios/roles$','view_roles',name = 'url_roles'),
            
    url(r'^usuarios/guardar$','view_saveusuario',name = 'url_saveusuario'),
    url(r'^usuarios/tipos/guardar$','view_savetipo',name = 'url_savetipo'),
    url(r'^usuarios/roles/guardar$','view_saverol',name = 'url_saverol'),           
                    
)


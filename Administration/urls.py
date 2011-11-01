from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Administration.views',
                       
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^usuarios/','view_usuarios',name = 'url_usuarios'),            
    url(r'^usuarios/guardar$','view_saveusuario',name = 'url_saveusuario'),           
                    
)
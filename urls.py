from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('views',
    # Examples:
    # url(r'^$', 'Transparencia.views.home', name='home'),
    # url(r'^Transparencia/', include('Transparencia.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    


    url(r'^$',redirect_to, {'url': 'transparencia/home/'},name = 'url_home'),
    url(r'^transparencia/home/$','view_home',name = 'url_home'),
    
    url(r'^transparencia/home/autenticar/$','view_autenticar', name = 'url_autenticar'),
    
    url(r'^transparencia/administracion/',include('Administration.urls')),
    url(r'^transparencia/encuesta/',include('Encuesta.urls')),
    url(r'^transparencia/reportes/',include('Reportes.urls')),
    
)

urlpatterns += staticfiles_urlpatterns()

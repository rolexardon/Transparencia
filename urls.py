from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.models import User, Group

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('views',

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    

    url(r'^$',redirect_to, {'url': 'transparencia/home/'},name = 'url_home'),
    url(r'^transparencia/home/$','view_home',name = 'url_home'),
    url(r'^transparencia/home/autenticar/$','view_autenticar', name = 'url_autenticar'),
    url(r'^transparencia/encuesta/',include('Encuesta.urls')),
    url(r'^transparencia/reportes/',include('Reportes.urls')),
    
    url(r'^transparencia/admin/goto/usuarios$','view_adminusuarios', name = 'url_adminusuarios'),
    url(r'^transparencia/admin/goto/segmentos$','view_adminsegmentos', name = 'url_adminsegmentos'),
    url(r'^transparencia/admin/goto/encuestas$','view_adminencuestas', name = 'url_adminencuestas'),
    #url(r'^transparencia/admin/goto/reportes$','view_adminreportes', name = 'url_adminreportes'),
    
    url(r'^transparencia/home/bring/encuestas$','view_bringencuestas',name = 'url_bringencuestas'),
    url(r'^transparencia/home/unpublish/encuesta/(?P<encuesta>\w+)$','view_despubencuestas',name = 'url_despubencuestas'),    
)

urlpatterns += staticfiles_urlpatterns()

#from django.conf.urls.defaults import patterns, include, url
from Transparencia.settings import DEBUG
from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.models import User, Group

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('views',

    url(r'^$',redirect_to, {'url': 'transparencia/login/'},name = 'url_login'),
    url(r'^transparencia/login/$','view_login',name = 'url_login'),
    url(r'^transparencia/logout/$','view_logout',name = 'url_logout'),
    url(r'^transparencia/home/$','view_home',name = 'url_home'),
    url(r'^transparencia/administracion/',include('Administration.urls')),
    url(r'^transparencia/encuesta/',include('Encuesta.urls')),
    url(r'^transparencia/reportes/',include('Reportes.urls')),
    
    url(r'^transparencia/admin/goto/usuarios$','view_adminusuarios', name = 'url_adminusuarios'),
    url(r'^transparencia/admin/goto/segmentos$','view_adminsegmentos', name = 'url_adminsegmentos'),
    url(r'^transparencia/admin/goto/encuestas$','view_adminencuestas', name = 'url_adminencuestas'),
    
    url(r'^transparencia/home/bring/encuestas$','view_bringencuestas',name = 'url_bringencuestas'),
    url(r'^transparencia/home/unpublish/encuesta/(?P<encuesta>\w+)$','view_despubencuestas',name = 'url_despubencuestas'),    

    #(r'^admin/', include('django.contrib.admin.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^imagenes_encuestas/(?P<path>.*)$', 
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),)


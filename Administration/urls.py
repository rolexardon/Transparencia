from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('Administration.views',
                       
    url(r'^gestionar/usuarios$','view_menuusuarios',name = 'url_menuusuarios'),
    url(r'^gestionar/segmentos$','view_gestionsegmentos',name = 'url_gestionsegmentos'),
	url(r'^gestionar/usuarios/bring$','view_bringusers',name = 'url_bringusers'),
    url(r'^gestionar/usuarios/delete(?P<pk>\d+)$','view_deleteuser',name = 'url_deleteuser'),
	url(r'^gestionar/segmentos/bring$','view_bringsegmento',name = 'url_bringsegmento'),
	url(r'^gestionar/usuarios/modificar/(?P<tipo>\w+)$','view_modificarusuario',name = 'url_modificarusuario'),
    url(r'^gestionar/usuarios/resetpwd/(?P<pk>\d+)$','view_pwdreset',name = 'url_pwdreset'),
	url(r'^gestionar/segmentos/modificar$','view_modificarsegmento',name = 'url_modificarsegmento'),

	

)
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from Encuesta.views import view_encuesta


urlpatterns = patterns('Reportes.views',
          
    url(r'^principal$','view_reporte',name = 'url_reporte'),             
    #url(r'^generar/','generar',name = 'generar'),
    
    url(r'^principal/bring/usuarios$','view_bringusuarios',name = 'url_bringusuarios'),    
    url(r'^principal/generar/reporte/estadistico$','view_reportestadistico',name = 'url_reportestadistico'),    
    url(r'^principal/generar/reporte/comparativo$','view_reportecomparativo',name = 'url_reportecomparativo'),
    
                       
)
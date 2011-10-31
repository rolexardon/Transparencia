from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to


urlpatterns = patterns('Encuesta.views',
                       
    url(r'^llenar/','view_encuesta',name = 'url_encuesta'),
    
    url(r'^bring/municipio$','view_bringmunicipio',name = 'url_bringmunicipio'),
    url(r'^bring/centros$','view_bringcentros',name = 'url_bringcentros'),
    url(r'^save/pg1$','view_savepg1',name = 'url_savepg1'),
    #url(r'^pagina1/','pagina1',name = 'pagina1'),
    #url(r'^pagina2/','pagina2',name = 'pagina2'), 
    #url(r'^pagina3/','pagina3',name = 'pagina3'), 
    #url(r'^pagina4/','pagina4',name = 'pagina4'),                        
                    
)
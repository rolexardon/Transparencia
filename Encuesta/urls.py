from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to


urlpatterns = patterns('Encuesta.views',
                       
    url(r'^encuesta/','view_encuesta',name = 'url_encuesta'),
    #url(r'^pagina1/','pagina1',name = 'pagina1'),
    #url(r'^pagina2/','pagina2',name = 'pagina2'), 
    #url(r'^pagina3/','pagina3',name = 'pagina3'), 
    #url(r'^pagina4/','pagina4',name = 'pagina4'),                        
                    
)
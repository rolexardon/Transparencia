from django.contrib import admin

from Transparencia.Encuesta.models import SegmentoA as SA
from Transparencia.Encuesta.models import SegmentoB as SB
from Transparencia.Encuesta.models import SegmentoC as SC
from Transparencia.Encuesta.models import SegmentoD as SD
from Transparencia.Encuesta.models import SegmentoE as SE
from Transparencia.Encuesta.models import SegmentoF as SF
from Transparencia.Encuesta.models import SegmentoG as SG
#from Transparencia.Encuesta.models import Encuesta as E
#from Transparencia.Encuesta.models import EncuestaData as ED
#from Transparencia.Encuesta.models import EncuestaTemp as ET
#from Transparencia.Encuesta.models import EncuestaTempData as ETD


class SegmentoA(admin.ModelAdmin):
    pass
class SegmentoB(admin.ModelAdmin):
    pass
class SegmentoC(admin.ModelAdmin):
    pass
class SegmentoD(admin.ModelAdmin):
    pass
class SegmentoE(admin.ModelAdmin):
    pass
class SegmentoF(admin.ModelAdmin):
    pass
class SegmentoG(admin.ModelAdmin):
    pass

admin.site.register(SA,SegmentoA)
admin.site.register(SB,SegmentoB)
admin.site.register(SC,SegmentoC)
admin.site.register(SD,SegmentoD)
admin.site.register(SE,SegmentoE)
admin.site.register(SF,SegmentoF)
admin.site.register(SG,SegmentoG)
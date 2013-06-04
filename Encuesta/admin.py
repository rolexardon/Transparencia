from django.contrib import admin
from Transparencia.Encuesta.models import SegmentoA as SA,SegmentoB as SB,SegmentoC as SC,SegmentoD as SD,SegmentoE as SE,SegmentoF as SF,SegmentoG as SG,EncuestaTemp as ET,EncuestaTempData as ETD,Encuesta as E,EncuestaData as ED,ListadoDocentesTemp as LDT,ListadoDocentes as LD


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
class EncuestaTemp(admin.ModelAdmin):
    pass
class EncuestaTempData(admin.ModelAdmin):
    pass
class Encuesta(admin.ModelAdmin):
    pass
class EncuestaData(admin.ModelAdmin):
    pass
class ListadoDocentesTemp(admin.ModelAdmin):
    pass
class ListadoDocentes(admin.ModelAdmin):
    pass

	
admin.site.register(SA,SegmentoA)
admin.site.register(SB,SegmentoB)
admin.site.register(SC,SegmentoC)
admin.site.register(SD,SegmentoD)
admin.site.register(SE,SegmentoE)
admin.site.register(SF,SegmentoF)
admin.site.register(SG,SegmentoG)
admin.site.register(ET,EncuestaTemp)
admin.site.register(ETD,EncuestaTempData)
admin.site.register(E,Encuesta)
admin.site.register(ED,EncuestaData)
admin.site.register(LDT,ListadoDocentesTemp)
admin.site.register(LD,ListadoDocentes)
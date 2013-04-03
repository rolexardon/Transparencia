from django.contrib import admin
from Transparencia.Administration.models import Usuario as U,TipoUsuario as TU,CentroEducativo as CE,Rol as R,Departamento as D,Municipio as M,Aldea as A,Caserio as CA,Barrio as B


class InfoUsuario(admin.ModelAdmin):
    pass
class TipoUsuario(admin.ModelAdmin):
    pass
class CentroEducativo(admin.ModelAdmin):
    pass
class Rol(admin.ModelAdmin):
    pass
class Departamento(admin.ModelAdmin):
    pass
class Municipio(admin.ModelAdmin):
    pass
class Aldea(admin.ModelAdmin):
    pass
class Caserio(admin.ModelAdmin):
    pass
class Barrio(admin.ModelAdmin):
    pass

	
admin.site.register(U,InfoUsuario)
admin.site.register(TU,TipoUsuario)
admin.site.register(CE,CentroEducativo)
admin.site.register(R,Rol)
admin.site.register(D,Departamento)
admin.site.register(M,Municipio)
admin.site.register(A,Aldea)
admin.site.register(CA,Caserio)
admin.site.register(B,Barrio)
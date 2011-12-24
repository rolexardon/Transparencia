from django.contrib import admin
from Transparencia.Administration.models import Usuario as US , TipoUsuario as TU

class InfoUsuario(admin.ModelAdmin):
    pass
class TipoUsuario(admin.ModelAdmin):
    pass

admin.site.register(US,InfoUsuario)
admin.site.register(TU,TipoUsuario)
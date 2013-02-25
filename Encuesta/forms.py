from django.forms import ModelForm
from Transparencia.Encuesta.models import SegmentoA as SA
from Transparencia.Encuesta.models import SegmentoB as SB
from Transparencia.Encuesta.models import SegmentoC as SC
from Transparencia.Encuesta.models import SegmentoD as SD
from Transparencia.Encuesta.models import SegmentoE as SE
from Transparencia.Encuesta.models import SegmentoF as SF
from Transparencia.Encuesta.models import SegmentoG as SG
from Transparencia.Encuesta.models import EncuestaTemp as ET
from Transparencia.Encuesta.models import Encuesta as E

class SAForm(ModelForm):
    class Meta:
        model = SA
        exclude = ('codigo')
        
class SBForm(ModelForm):
    class Meta:
        model = SB
        exclude = ('codigo')
        
class SCForm(ModelForm):
    class Meta:
        model = SC
        exclude = ('codigo')
        
class SDForm(ModelForm):
    class Meta:
        model = SD
        exclude = ('codigo')
        
class SEForm(ModelForm):
    class Meta:
        model = SE
        exclude = ('codigo')
        
class SFForm(ModelForm):
    class Meta:
        model = SF
        exclude = ('codigo')
        
class SGForm(ModelForm):
    class Meta:
        model = SG
        exclude = ('codigo')

class ET_Form(ModelForm):
    class Meta:
        model = ET
        exclude = ('codigo', 'fecha_apertura','fecha','codigo_usuario','codigo_centro','zona','tel', 'observacion', 'alumnos')

class E_Form(ModelForm):
    class Meta:
        model = E
        exclude = ('codigo', 'fecha_apertura','fecha','codigo_usuario','codigo_departamento','codigo_municipio','codigo_centro','zona','tel', 'observacion', 'alumnos')
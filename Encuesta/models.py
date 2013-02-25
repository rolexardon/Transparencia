from django.db import models
from Transparencia.Administration import models as AdMod
from django.db.models import Avg, Max, Min, Count
from django.contrib.auth.models import User 

# Create your models here.
class SegmentoA(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoA):
        return SegmentoA.objects.all().order_by('codigo')
        
 #   def __unicode__(self):
 #       return self.BringAll
    def __unicode__(self):
        return self.descripcion
    
class SegmentoB(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoB):
        return SegmentoB.objects.all().order_by('codigo')
        
 #   def __unicode__(self):
 #       return self.BringAll
    def __unicode__(self):
        return self.descripcion

class SegmentoC(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoC):
        return SegmentoC.objects.all().order_by('codigo')
        
 #   def __unicode__(self):
 #       return self.BringAll
    def __unicode__(self):
        return self.descripcion

class SegmentoD(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoD):
        return SegmentoD.objects.all().order_by('codigo')
        
 #   def __unicode__(self):
 #       return self.BringAll
    def __unicode__(self):
        return self.descripcion
        
class SegmentoE(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoE):
        return SegmentoE.objects.all().order_by('codigo')
        
 #   def __unicode__(self):
 #       return self.BringAll
    def __unicode__(self):
        return self.descripcion
    
class SegmentoF(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoF):
        return SegmentoF.objects.all().order_by('codigo')
        
 #   def __unicode__(self):
 #       return self.BringAll
    def __unicode__(self):
        return self.descripcion

class SegmentoG(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoG):
        return SegmentoG.objects.all().order_by('codigo')
        
 #   def __unicode__(self):
 #       return self.BringAll
    def __unicode__(self):
        return self.descripcion
    

class EncuestaTemp(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha_apertura = models.DateField(null=True,blank=True)
    fecha = models.DateField(null=True,blank=True)
    codigo_usuario = models.ForeignKey(User)
    codigo_centro = models.ForeignKey(AdMod.CentroEducativo, null = True, blank = True,default = None)
    zona = models.CharField(max_length=50,null=True,blank=True,default=None)
    tel = models.IntegerField(null=True,blank=True)
    observacion = models.CharField(max_length=300,null=True,blank=True,default="")
    alumnos = models.IntegerField(null=True,blank=True,default=0)
    imagen01 = models.ImageField(upload_to='imagenes_%d%m%Y',null = True)
    imagen02 = models.ImageField(upload_to='imagenes_%d%m%Y',null = True)
    
class EncuestaTempData(models.Model):
    encuesta = models.ForeignKey(EncuestaTemp)
    segmento = models.CharField(max_length=2 ,blank=True)
    codigo_item = models.IntegerField(null=True,blank=True,default=0)
    tipo_valor = models.CharField(max_length = 100,null= True,blank=True)
    valor_item =  models.CharField(max_length = 255,null= True,blank=True)
                
class Encuesta(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha_apertura = models.DateField()
    fecha = models.DateField()
    codigo_usuario = models.ForeignKey(User)
    codigo_departamento = models.ForeignKey(AdMod.Departamento)
    codigo_municipio = models.ForeignKey(AdMod.Municipio)
    codigo_centro = models.ForeignKey(AdMod.CentroEducativo)
    zona = models.CharField(max_length=50)
    tel = models.IntegerField()
    observacion = models.CharField(max_length=300,default="")
    alumnos = models.IntegerField()
    imagen01 = models.ImageField(upload_to='imagenes_%d%m%Y',null=True,default=None)
    imagen02 = models.ImageField(upload_to='imagenes_%d%m%Y',null=True,default=None)
    
class EncuestaData(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    segmento = models.CharField(max_length=2)
    codigo_item = models.IntegerField()
    tipo_valor = models.CharField(max_length = 100)
    valor_item =  models.CharField(max_length = 255)
    
    
    @classmethod
    def BringValue(EncuestaData,enc,seg,cod):
        return EncuestaData.objects.get(encuesta = enc, segmento = seg, codigo_item = cod).valor_item
        
    def __unicode__(self):
        return self.BringAll
    
class ListadoDocentesTemp(models.Model):
    encuesta = models.ForeignKey(EncuestaTemp)
    segmento = models.CharField(max_length=2)
    id_personal =  models.CharField(max_length = 255)
    nombre =  models.CharField(max_length = 255)
    
    @classmethod
    def BringAll(ListadoDocentesTemp,encuesta,segmento):
        return ListadoDocentesTemp.objects.filter(encuesta = encuesta, segmento = segmento)
        
    def __unicode__(self):
        return self.BringAll
 #   def __unicode__(self):
#      return self.descripcion
    
class ListadoDocentes(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    segmento = models.CharField(max_length=2)
    id_personal =  models.CharField(max_length = 255)
    nombre =  models.CharField(max_length = 255)
    
    @classmethod
    def BringAll(ListadoDocentes,encuesta,segmento):
        return ListadoDocentes.objects.filter(encuesta = encuesta, segmento = segmento)
        
    def __unicode__(self):
        return self.BringAll
    
    
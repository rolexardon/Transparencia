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
        return SegmentoA.objects.all()
        
    def __unicode__(self):
        return self.BringAll
    
class SegmentoB(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoB):
        return SegmentoB.objects.all()
        
    def __unicode__(self):
        return self.BringAll

class SegmentoC(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoC):
        return SegmentoC.objects.all()
        
    def __unicode__(self):
        return self.BringAll

class SegmentoD(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoD):
        return SegmentoD.objects.all()
        
    def __unicode__(self):
        return self.BringAll
        
class SegmentoE(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoE):
        return SegmentoE.objects.all()
        
    def __unicode__(self):
        return self.BringAll
    
class SegmentoF(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoF):
        return SegmentoF.objects.all()
        
    def __unicode__(self):
        return self.BringAll

class SegmentoG(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 255, unique = True)
    
    @classmethod
    def BringAll(SegmentoG):
        return SegmentoG.objects.all()
        
    def __unicode__(self):
        return self.BringAll
    

class EncuestaTemp(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True,blank=True)
    codigo_usuario = models.ForeignKey(User)
    codigo_centro = models.ForeignKey(AdMod.CentroEducativo, null = True, blank = True,default = None)
    
class EncuestaTempData(models.Model):
    encuesta = models.ForeignKey(EncuestaTemp)
    segmento = models.CharField(max_length=2 ,null=True,blank=True,default="")
    codigo_item = models.IntegerField(null=True,blank=True,default=0)
    tipo_valor = models.CharField(max_length = 100,null= True,blank=True)
    valor_item =  models.CharField(max_length = 255,null= True,blank=True)
                
class Encuesta(models.Model):
    codigo = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    codigo_usuario = models.ForeignKey(User)
    codigo_centro = models.ForeignKey(AdMod.CentroEducativo)
        
class EncuestaData(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    codigo_segmento = models.IntegerField()
    codigo_item = models.IntegerField()
    tipo_valor = models.CharField(max_length = 100)
    valor_item =  models.CharField(max_length = 255)
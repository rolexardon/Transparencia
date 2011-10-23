from django.db import models
from Transparencia.Administration import models as AdMod

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
    
class EncuestaSegementoB(models.Model):
    codigo_encuesta = models.IntegerField()
    codigo = models.ForeignKey(SegmentoB)
class EncuestaSegementoF(models.Model):
    codigo_encuesta = models.IntegerField()
    codigo = models.ForeignKey(SegmentoF)
    
class Encuesta(models.Model):
    fecha = models.DateField()
    codigo_usuario = models.ForeignKey(AdMod.Usuario)
    codigo_centro = models.ForeignKey(AdMod.CentroEducativo)
    ubicacion = models.CharField(max_length = 300)
    codigo_segmentob = models.IntegerField(unique=True)
    segmentob_extras = models.IntegerField(unique= True)
    c1 = models.BooleanField()
    c2 = models.BooleanField()
    c3 = models.BooleanField()
    d1 = models.IntegerField()
    d2 = models.IntegerField()
    d3 = models.IntegerField()
    e1 = models.IntegerField()
    e2 = models.IntegerField()
    e3 = models.IntegerField()
    e4 = models.IntegerField()
    e5 = models.IntegerField()
    e6 = models.IntegerField()
    e7 = models.IntegerField()
    codigo_segmentof = models.IntegerField(unique=True)
    segmentof_extras = models.IntegerField(unique=True)
    g1 = models.CharField(max_length=200)
    g2 = models.CharField(max_length=200)
    g3 = models.CharField(max_length=200)
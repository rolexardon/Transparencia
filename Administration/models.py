from django.db import models
from django.forms.widgets import PasswordInput


class CentroEducativo(models.Model):
    #codigo = models.AutoField(primary_key=True)
    codigo_departamento = models.CharField(max_length=100)
    descripcion_departamento = models.CharField(max_length=300)
    codigo_municipio = models.CharField(max_length=100)
    descripcion_municipio = models.CharField(max_length=300)
    codigo_ce = models.CharField(max_length=100)
    nombre = models.CharField(max_length=300)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=100)
    tipo_centro = models.CharField(max_length=300)
    administracion = models.CharField(max_length=300)
    
    @classmethod
    def BringAll(CentroEducativo):
        return CentroEducativo.objects.all()
    @classmethod
    def FilterByDepMun(CentroEducativo,dep,mun):
        return CentroEducativo.objects.filter(Codigo_Departamento = dep, Codigo_Municipio = mun)
    
    def __unicode__(self):
        return self.BringAll
    
class TipoUsuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 200)

class Rol(models.Model):
    codigo = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    
class Departamento(models.Model):
    codigo = models.CharField(max_length=2,unique=True)
    nombre = models.CharField(max_length=100,unique=True)
    
    @classmethod
    def BringAll(Departamento):
        return Departamento.objects.all()
        
    def __unicode__(self):
        return self.BringAll

class Municipio(models.Model):
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento)
    
    @classmethod
    def BringAll(Municipio):
        return Municipio.objects.all()
    @classmethod    
    def FilterByDep(Municipio,dep):
        return Municipio.objects.filter(departamento_id = dep)
        
    def __unicode__(self):
        return self.BringAll
    
class Aldea(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=300)
    municipio = models.ForeignKey(Municipio)
    
class Caserio(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=300)
    aldea = models.ForeignKey(Aldea)
    
class Barrio(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=300)
    caserio = models.ForeignKey(Caserio)
    
class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=200)
    usuario = models.CharField(max_length=100,unique=True)
    #password = models.CharField(max_length=50,unique=True,widget=PasswordInput(render_value=False))
    password = models.CharField(max_length=50,unique=True)
    tipo_usuario = models.ForeignKey(TipoUsuario)
    telefono = models.CharField(max_length = 10)
    email = models.EmailField()
    municipio = models.ForeignKey(Municipio)
    rol = models.ForeignKey(Rol)
    activo = models.BooleanField(default = True)
# Create your models here.

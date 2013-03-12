# -*- coding: latin-1 -*-
from django.db import models
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save

class CentroEducativo(models.Model):
    
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
        if len(str(dep)) == 1:
            dep = '0' + str(dep)
        if len(str(mun)) == 1:
            mun = '0' + str(mun)
           
        return CentroEducativo.objects.filter(codigo_departamento = str(dep), codigo_municipio = str(mun)).order_by('nombre')
    @classmethod
    def GetCodigoCentro(CentroEducativo,idcentro):
        try:
            return CentroEducativo.objects.get(pk=idcentro).codigo_ce
        except:
            return ""
    @classmethod
    def GetTipoCentro(CentroEducativo,idcentro):
        try:
            return CentroEducativo.objects.get(pk=idcentro).tipo_centro
        except:
            return ""
    def __unicode__(self):
        return self.nombre
    
class TipoUsuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 200)
    
    @classmethod
    def BringAll(TipoUsuario):
        return TipoUsuario.objects.all()

    def __unicode__(self):
        return self.nombre

class Rol(models.Model):
    codigo = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length = 200)

    @classmethod
    def BringAll(Rol):
        return Rol.objects.all()
    
    def __unicode__(self):
        return self.nombre
    
class Departamento(models.Model):
    codigo = models.CharField(max_length=2,unique=True)
    nombre = models.CharField(max_length=100,unique=True)
    
    @classmethod
    def BringAll(Departamento):
        return Departamento.objects.all()
        
    #def __unicode__(self):
     #   return self.BringAll
    
    def __unicode__(self):
        return self.nombre

class Municipio(models.Model):
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento)
    
    @classmethod
    def BringAll(Municipio):
        return Municipio.objects.all()
    @classmethod    
    def FilterByDep(Municipio,dep):
        return Municipio.objects.filter(departamento = dep)
    @classmethod
    def BringDepId(Municipio,id):
        return Municipio.objects.get(pk=id).departamento.pk
    @classmethod
    def BringMunCode(Municipio,k):
        p = Municipio.get(pk=k)
        return p.codigo   
    def __unicode__(self):
        return self.nombre
    
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
    
#class Usuario(models.Model):
class Usuario(User):
    
    #user = models.OneToOneField(User)
    
    tipo_usuario = models.ForeignKey(TipoUsuario, null = True, blank = True,default = None)
    telefono = models.CharField(max_length = 10, null = True, blank = True,default = None)
    direccion = models.CharField(max_length = 500, null = True, blank = True,default = None)
    rol = models.ForeignKey(Rol,  null = True, blank = True,default = None)
    
    objects = UserManager()
    #user = models.ForeignKey(User, unique=True)

   # def __unicode__(self):
    #    return self.user.username

    
    @classmethod
    def BringAll(Usuario):
        return Usuario.objects.filter(is_active=1)
    @classmethod 
    def BringByTipo(Usuario,tipo):
        tipousuario = TipoUsuario.objects.get(codigo = tipo)
        #user = getattr(User, 'tipo_usuario', None)
        #usuarios=Usuario.objects.filter(tipo_usuario = tipousuario)
        usuarios=Usuario.objects.filter(tipo_usuario = tipousuario)
        return usuarios
    @classmethod 
    def BringByTipo_Username(Usuario,tipo,un):
        if tipo:
            if un:
                #tipousuario = TipoUsuario.objects.get(codigo = tipo)
                #user = getattr(Usuario, 'tipo_usuario', None)
                usuarios=Usuario.objects.filter(tipo_usuario = tipo,username__contains=un,is_active=1)
            else:
                #tipousuario = TipoUsuario.objects.get(codigo = tipo)
                #user = getattr(Usuario, 'tipo_usuario', None)
                usuarios=Usuario.objects.filter(tipo_usuario = tipo,is_active=1)
        else:
            if un:
                usuarios=Usuario.objects.filter(username__contains=un,is_active=1)
             #usuarios=User.objects.filter(username__contains=un,is_active=1)
             
            else:
                usuarios=Usuario.objects.filter(is_active=1)
             #usuarios=User.objects.filter(is_active=1)
        print usuarios
        return usuarios




# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CentroEducativo'
        db.create_table('Administration_centroeducativo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_departamento', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion_departamento', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('codigo_municipio', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion_municipio', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('codigo_ce', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tipo_centro', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('administracion', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('Administration', ['CentroEducativo'])

        # Adding model 'TipoUsuario'
        db.create_table('Administration_tipousuario', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('Administration', ['TipoUsuario'])

        # Adding model 'Rol'
        db.create_table('Administration_rol', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('Administration', ['Rol'])

        # Adding model 'Departamento'
        db.create_table('Administration_departamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('Administration', ['Departamento'])

        # Adding model 'Municipio'
        db.create_table('Administration_municipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administration.Departamento'])),
        ))
        db.send_create_signal('Administration', ['Municipio'])

        # Adding model 'Aldea'
        db.create_table('Administration_aldea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administration.Municipio'])),
        ))
        db.send_create_signal('Administration', ['Aldea'])

        # Adding model 'Caserio'
        db.create_table('Administration_caserio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('aldea', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administration.Aldea'])),
        ))
        db.send_create_signal('Administration', ['Caserio'])

        # Adding model 'Barrio'
        db.create_table('Administration_barrio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('caserio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administration.Caserio'])),
        ))
        db.send_create_signal('Administration', ['Barrio'])

        # Adding model 'Usuario'
        db.create_table('Administration_usuario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administration.TipoUsuario'])),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('rol', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administration.Rol'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('Administration', ['Usuario'])


    def backwards(self, orm):
        
        # Deleting model 'CentroEducativo'
        db.delete_table('Administration_centroeducativo')

        # Deleting model 'TipoUsuario'
        db.delete_table('Administration_tipousuario')

        # Deleting model 'Rol'
        db.delete_table('Administration_rol')

        # Deleting model 'Departamento'
        db.delete_table('Administration_departamento')

        # Deleting model 'Municipio'
        db.delete_table('Administration_municipio')

        # Deleting model 'Aldea'
        db.delete_table('Administration_aldea')

        # Deleting model 'Caserio'
        db.delete_table('Administration_caserio')

        # Deleting model 'Barrio'
        db.delete_table('Administration_barrio')

        # Deleting model 'Usuario'
        db.delete_table('Administration_usuario')


    models = {
        'Administration.aldea': {
            'Meta': {'object_name': 'Aldea'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Administration.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'Administration.barrio': {
            'Meta': {'object_name': 'Barrio'},
            'caserio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Administration.Caserio']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'Administration.caserio': {
            'Meta': {'object_name': 'Caserio'},
            'aldea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Administration.Aldea']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'Administration.centroeducativo': {
            'Meta': {'object_name': 'CentroEducativo'},
            'administracion': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'codigo_ce': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'codigo_departamento': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'codigo_municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'descripcion_departamento': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'descripcion_municipio': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tipo_centro': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'Administration.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'Administration.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Administration.Departamento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'Administration.rol': {
            'Meta': {'object_name': 'Rol'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'Administration.tipousuario': {
            'Meta': {'object_name': 'TipoUsuario'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'Administration.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Administration.Rol']"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tipo_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Administration.TipoUsuario']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Administration']

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Encuesta'
        db.delete_table('Encuesta_encuesta')

        # Deleting model 'EncuestaData'
        db.delete_table('Encuesta_encuestadata')


    def backwards(self, orm):
        
        # Adding model 'Encuesta'
        db.create_table('Encuesta_encuesta', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('codigo_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('codigo_centro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administration.CentroEducativo'])),
        ))
        db.send_create_signal('Encuesta', ['Encuesta'])

        # Adding model 'EncuestaData'
        db.create_table('Encuesta_encuestadata', (
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Encuesta.Encuesta'])),
            ('valor_item', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('codigo_item', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_valor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('codigo_segmento', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('Encuesta', ['EncuestaData'])


    models = {
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
        'Encuesta.encuestatemp': {
            'Meta': {'object_name': 'EncuestaTemp'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'codigo_centro': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['Administration.CentroEducativo']", 'null': 'True', 'blank': 'True'}),
            'codigo_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'Encuesta.encuestatempdata': {
            'Meta': {'object_name': 'EncuestaTempData'},
            'codigo_item': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Encuesta.EncuestaTemp']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'segmento': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'tipo_valor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'valor_item': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'Encuesta.segmentoa': {
            'Meta': {'object_name': 'SegmentoA'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'Encuesta.segmentob': {
            'Meta': {'object_name': 'SegmentoB'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'Encuesta.segmentoc': {
            'Meta': {'object_name': 'SegmentoC'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'Encuesta.segmentod': {
            'Meta': {'object_name': 'SegmentoD'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'Encuesta.segmentoe': {
            'Meta': {'object_name': 'SegmentoE'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'Encuesta.segmentof': {
            'Meta': {'object_name': 'SegmentoF'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'Encuesta.segmentog': {
            'Meta': {'object_name': 'SegmentoG'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
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

    complete_apps = ['Encuesta']

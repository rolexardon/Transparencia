# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Encuesta.observacion'
        db.add_column('Encuesta_encuesta', 'observacion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300),
                      keep_default=False)

        # Adding field 'EncuestaTemp.observacion'
        db.add_column('Encuesta_encuestatemp', 'observacion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Encuesta.observacion'
        db.delete_column('Encuesta_encuesta', 'observacion')

        # Deleting field 'EncuestaTemp.observacion'
        db.delete_column('Encuesta_encuestatemp', 'observacion')


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
        'Encuesta.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'codigo_centro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Administration.CentroEducativo']"}),
            'codigo_departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Administration.Departamento']"}),
            'codigo_municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Administration.Municipio']"}),
            'codigo_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fecha_apertura': ('django.db.models.fields.DateField', [], {}),
            'observacion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            'tel': ('django.db.models.fields.IntegerField', [], {}),
            'zona': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'Encuesta.encuestadata': {
            'Meta': {'object_name': 'EncuestaData'},
            'codigo_item': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'segmento': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'tipo_valor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valor_item': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'Encuesta.encuestatemp': {
            'Meta': {'object_name': 'EncuestaTemp'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'codigo_centro': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['Administration.CentroEducativo']", 'null': 'True', 'blank': 'True'}),
            'codigo_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_apertura': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'observacion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'tel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zona': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'Encuesta.encuestatempdata': {
            'Meta': {'object_name': 'EncuestaTempData'},
            'codigo_item': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Encuesta.EncuestaTemp']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'segmento': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'tipo_valor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'valor_item': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'Encuesta.listadodocentes': {
            'Meta': {'object_name': 'ListadoDocentes'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_personal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'segmento': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'Encuesta.listadodocentestemp': {
            'Meta': {'object_name': 'ListadoDocentesTemp'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Encuesta.EncuestaTemp']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_personal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'segmento': ('django.db.models.fields.CharField', [], {'max_length': '2'})
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
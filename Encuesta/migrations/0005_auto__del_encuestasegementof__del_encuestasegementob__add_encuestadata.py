# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'EncuestaSegementoF'
        db.delete_table('Encuesta_encuestasegementof')

        # Deleting model 'EncuestaSegementoB'
        db.delete_table('Encuesta_encuestasegementob')

        # Adding model 'EncuestaData'
        db.create_table('Encuesta_encuestadata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Encuesta.Encuesta'])),
            ('codigo_segmento', self.gf('django.db.models.fields.IntegerField')()),
            ('codigo_item', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo_valor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('valor_item', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('Encuesta', ['EncuestaData'])

        # Adding model 'EncuestaTempData'
        db.create_table('Encuesta_encuestatempdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Encuesta.EncuestaTemp'])),
            ('codigo_segmento', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('codigo_item', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('tipo_valor', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('valor_item', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('Encuesta', ['EncuestaTempData'])

        # Deleting field 'Encuesta.codigo_item'
        db.delete_column('Encuesta_encuesta', 'codigo_item')

        # Deleting field 'Encuesta.tipo_valor'
        db.delete_column('Encuesta_encuesta', 'tipo_valor')

        # Deleting field 'Encuesta.valor_item'
        db.delete_column('Encuesta_encuesta', 'valor_item')

        # Deleting field 'Encuesta.codigo_segmento'
        db.delete_column('Encuesta_encuesta', 'codigo_segmento')

        # Deleting field 'EncuestaTemp.codigo_item'
        db.delete_column('Encuesta_encuestatemp', 'codigo_item')

        # Deleting field 'EncuestaTemp.tipo_valor'
        db.delete_column('Encuesta_encuestatemp', 'tipo_valor')

        # Deleting field 'EncuestaTemp.valor_item'
        db.delete_column('Encuesta_encuestatemp', 'valor_item')

        # Deleting field 'EncuestaTemp.codigo_segmento'
        db.delete_column('Encuesta_encuestatemp', 'codigo_segmento')


    def backwards(self, orm):
        
        # Adding model 'EncuestaSegementoF'
        db.create_table('Encuesta_encuestasegementof', (
            ('codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Encuesta.SegmentoF'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_encuesta', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('Encuesta', ['EncuestaSegementoF'])

        # Adding model 'EncuestaSegementoB'
        db.create_table('Encuesta_encuestasegementob', (
            ('codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Encuesta.SegmentoB'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_encuesta', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('Encuesta', ['EncuestaSegementoB'])

        # Deleting model 'EncuestaData'
        db.delete_table('Encuesta_encuestadata')

        # Deleting model 'EncuestaTempData'
        db.delete_table('Encuesta_encuestatempdata')

        # Adding field 'Encuesta.codigo_item'
        db.add_column('Encuesta_encuesta', 'codigo_item', self.gf('django.db.models.fields.IntegerField')(default=datetime.date(2011, 11, 12)), keep_default=False)

        # Adding field 'Encuesta.tipo_valor'
        db.add_column('Encuesta_encuesta', 'tipo_valor', self.gf('django.db.models.fields.CharField')(default=datetime.date(2011, 11, 12), max_length=100), keep_default=False)

        # Adding field 'Encuesta.valor_item'
        db.add_column('Encuesta_encuesta', 'valor_item', self.gf('django.db.models.fields.CharField')(default=datetime.date(2011, 11, 12), max_length=255), keep_default=False)

        # Adding field 'Encuesta.codigo_segmento'
        db.add_column('Encuesta_encuesta', 'codigo_segmento', self.gf('django.db.models.fields.IntegerField')(default=datetime.date(2011, 11, 12)), keep_default=False)

        # Adding field 'EncuestaTemp.codigo_item'
        db.add_column('Encuesta_encuestatemp', 'codigo_item', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'EncuestaTemp.tipo_valor'
        db.add_column('Encuesta_encuestatemp', 'tipo_valor', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'EncuestaTemp.valor_item'
        db.add_column('Encuesta_encuestatemp', 'valor_item', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'EncuestaTemp.codigo_segmento'
        db.add_column('Encuesta_encuestatemp', 'codigo_segmento', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)


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
        'Encuesta.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'codigo': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'codigo_centro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Administration.CentroEducativo']"}),
            'codigo_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'fecha': ('django.db.models.fields.DateField', [], {})
        },
        'Encuesta.encuestadata': {
            'Meta': {'object_name': 'EncuestaData'},
            'codigo_item': ('django.db.models.fields.IntegerField', [], {}),
            'codigo_segmento': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_valor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valor_item': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'codigo_segmento': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Encuesta.EncuestaTemp']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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

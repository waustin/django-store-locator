# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ZipCodeLocation'
        db.create_table(u'store_locator_zipcodelocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=7, db_index=True)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'store_locator', ['ZipCodeLocation'])

        # Adding model 'Location'
        db.create_table(u'store_locator_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=125, db_index=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=10, db_index=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=5, db_index=True)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'store_locator', ['Location'])


    def backwards(self, orm):
        # Deleting model 'ZipCodeLocation'
        db.delete_table(u'store_locator_zipcodelocation')

        # Deleting model 'Location'
        db.delete_table(u'store_locator_location')


    models = {
        u'store_locator.location': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '125', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_index': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'})
        },
        u'store_locator.zipcodelocation': {
            'Meta': {'object_name': 'ZipCodeLocation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'zip_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '7', 'db_index': 'True'})
        }
    }

    complete_apps = ['store_locator']
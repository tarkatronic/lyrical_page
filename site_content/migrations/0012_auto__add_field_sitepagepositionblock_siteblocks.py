# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SitePagePositionBlock.siteblocks'
        db.add_column('site_content_sitepagepositionblock', 'siteblocks',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['site_content.SiteBlock']),
                      keep_default=False)

        # Removing M2M table for field siteblocks on 'SitePagePositionBlock'
        db.delete_table('site_content_sitepagepositionblock_siteblocks')

    def backwards(self, orm):
        # Deleting field 'SitePagePositionBlock.siteblocks'
        db.delete_column('site_content_sitepagepositionblock', 'siteblocks_id')

        # Adding M2M table for field siteblocks on 'SitePagePositionBlock'
        db.create_table('site_content_sitepagepositionblock_siteblocks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sitepagepositionblock', models.ForeignKey(orm['site_content.sitepagepositionblock'], null=False)),
            ('siteblock', models.ForeignKey(orm['site_content.siteblock'], null=False))
        ))
        db.create_unique('site_content_sitepagepositionblock_siteblocks', ['sitepagepositionblock_id', 'siteblock_id'])

    models = {
        'site_content.siteblock': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'SiteBlock'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enable_rte': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'siteposition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePosition']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'site_content.sitemenu': {
            'Meta': {'object_name': 'SiteMenu'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'site_content.sitemenuitem': {
            'Meta': {'object_name': 'SiteMenuItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'sitemenu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SiteMenu']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'site_content.sitepage': {
            'Meta': {'unique_together': "(('site', 'url'),)", 'object_name': 'SitePage'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'page_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'sitemenu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SiteMenu']", 'null': 'True', 'blank': 'True'}),
            'sitemenu_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sitemenu_weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'site_content.sitepagealias': {
            'Meta': {'object_name': 'SitePageAlias'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sitepage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePage']"}),
            'url_alias': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'site_content.sitepagepositionblock': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'SitePagePositionBlock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'siteblocks': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SiteBlock']"}),
            'sitepage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePage']"}),
            'siteposition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePosition']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'site_content.sitepageredirect': {
            'Meta': {'object_name': 'SitePageRedirect'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sitepage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['site_content.SitePage']"}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'site_content.siteposition': {
            'Meta': {'object_name': 'SitePosition'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['site_content']

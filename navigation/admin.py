# -*- coding:utf-8 -*-
from django.contrib import admin
from models import Subdivision, Redirect
from modeltranslation.admin import TranslationAdmin

import navigation.translation


class AdminSubdivision(TranslationAdmin):
    list_display = ('name', 'parent', 'priority', 'address', 'pageView', 'show', 'published')
    list_editable = ['parent', 'priority', 'address', 'pageView', 'show', 'published']
'''
    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            '/static/grappelli_modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/grappelli_modeltranslation/css/tabbed_translation_fields.css',),
        }
'''
admin.site.register(Subdivision, AdminSubdivision)
admin.site.register(Redirect)
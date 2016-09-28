# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from .models import Subdivision


class SubdivisionTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'keywords', 'title', 'before', 'after', 'pageTitle')

translator.register(Subdivision, SubdivisionTranslationOptions)


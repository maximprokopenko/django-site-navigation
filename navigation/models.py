# -*- coding:utf-8 -*-
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.core.validators import URLValidator

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField as HTMLField


class Subdivision(models.Model):
    name = models.CharField(u'Название в меню', max_length=255)
    pageTitle = models.CharField(u'Название на сранице', blank=True, null=True, max_length=255)
    parent = models.ForeignKey('Subdivision', blank=True, null=True, verbose_name=u'Родитель')
    priority = models.IntegerField(u'Приоритет', blank=True)
    address = models.CharField(u'Address', max_length=255)
    description = models.CharField(u'Description', max_length=255, blank=True, null=True,)
    keywords = models.CharField(u'Keywords', max_length=255, blank=True, null=True,)
    title = models.CharField(u'Title', max_length=255, blank=True, null=True,)
    link = models.CharField(u'Link', max_length=255, blank=True, null=True,)
    show = models.BooleanField(u'Отображать в меню', blank=True, default=None)
    published = models.BooleanField(u'Опубликовано', default=True)
    kwards = models.CharField(u'kwards', blank=True, null=True, max_length=255)
    pageview = models.CharField(u'Предстовление', blank=True, null=True, max_length=255)
    before = HTMLField(u'Текст до', blank=True, null=True,)
    after = HTMLField(u'Текст после', blank=True, null=True,)

    def __url__(self):
        path = ''
        if(self.parent):
            path += self.parent.__url__() + '/'
        path += self.address
        return path

    def getUrl(self):
        if '.' in self.address:
            return '/' + self.__url__()
        else:
            return '/' + self.__url__() + '/'

    def save(self):

        if not self.priority:
            maxPriority = Subdivision.objects.aggregate(Max('priority'))['priority__max']

            if maxPriority:
                self.priority = maxPriority + 1
            else:
                self.priority = 1

        if self.address == '/':
            self.parent = None

        super(Subdivision, self).save()

    class Meta:
        verbose_name = u'Раздел'
        verbose_name_plural = u'Разделы'
        unique_together = (("parent", "name"),
                           ("parent", "address"),)
        ordering = ('-priority',)

    def __unicode__(self):
        return self.name


class Redirect(models.Model):
    url_from = models.CharField(u'from', max_length=255, validators=[URLValidator,], unique=True)
    url_to = models.CharField(u'to', max_length=255, validators=[URLValidator,])

    def __unicode__(self):
        return self.url_from[:50]

    class Meta:
        verbose_name = u'Редирект'
        verbose_name_plural = u'Редиректы'

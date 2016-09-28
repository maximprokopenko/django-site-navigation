# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432 \u043c\u0435\u043d\u044e')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432 \u043c\u0435\u043d\u044e')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432 \u043c\u0435\u043d\u044e')),
                ('pageTitle', models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u0430 \u0441\u0440\u0430\u043d\u0438\u0446\u0435', blank=True)),
                ('pageTitle_ru', models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u0430 \u0441\u0440\u0430\u043d\u0438\u0446\u0435', blank=True)),
                ('pageTitle_en', models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u0430 \u0441\u0440\u0430\u043d\u0438\u0446\u0435', blank=True)),
                ('priority', models.IntegerField(verbose_name='\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442', blank=True)),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Description', blank=True)),
                ('description_ru', models.CharField(max_length=255, null=True, verbose_name='Description', blank=True)),
                ('description_en', models.CharField(max_length=255, null=True, verbose_name='Description', blank=True)),
                ('keywords', models.CharField(max_length=255, null=True, verbose_name='Keywords', blank=True)),
                ('keywords_ru', models.CharField(max_length=255, null=True, verbose_name='Keywords', blank=True)),
                ('keywords_en', models.CharField(max_length=255, null=True, verbose_name='Keywords', blank=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Title', blank=True)),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Title', blank=True)),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Title', blank=True)),
                ('link', models.CharField(max_length=255, null=True, verbose_name='Link', blank=True)),
                ('show', models.BooleanField(default=None, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0432 \u043c\u0435\u043d\u044e')),
                ('published', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
                ('kwards', models.CharField(max_length=255, null=True, verbose_name='kwards', blank=True)),
                ('pageview', models.CharField(max_length=255, null=True, verbose_name='\u041f\u0440\u0435\u0434\u0441\u0442\u043e\u0432\u043b\u0435\u043d\u0438\u0435', blank=True)),
                ('before', ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043e', blank=True)),
                ('before_ru', ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043e', blank=True)),
                ('before_en', ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043e', blank=True)),
                ('after', ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435', blank=True)),
                ('after_ru', ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435', blank=True)),
                ('after_en', ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435', blank=True)),
                ('parent', models.ForeignKey(verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c', blank=True, to='navigation.Subdivision', null=True)),
            ],
            options={
                'ordering': ('-priority',),
                'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b',
                'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='subdivision',
            unique_together=set([('parent', 'address'), ('parent', 'name')]),
        ),
    ]

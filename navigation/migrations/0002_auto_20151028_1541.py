# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdivision',
            name='after',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='after_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='after_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='before',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043e', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='before_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043e', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='before_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043e', blank=True),
            preserve_default=True,
        ),
    ]

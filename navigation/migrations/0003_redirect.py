# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_auto_20151028_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_from', models.CharField(unique=True, max_length=255, verbose_name='from', validators=[django.core.validators.URLValidator])),
                ('url_to', models.CharField(max_length=255, verbose_name='to', validators=[django.core.validators.URLValidator])),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0434\u0438\u0440\u0435\u043a\u0442',
                'verbose_name_plural': '\u0420\u0435\u0434\u0438\u0440\u0435\u043a\u0442',
            },
            bases=(models.Model,),
        ),
    ]

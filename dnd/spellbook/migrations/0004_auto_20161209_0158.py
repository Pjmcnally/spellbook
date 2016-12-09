# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0003_auto_20161205_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='cast_time_text',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spell',
            name='component_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spell',
            name='range_text',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CastingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(help_text='A label for URL config', max_length=100, unique=True)),
            ],
            options={
                'ordering': ['text'],
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(help_text='A lable for URL config', max_length=20, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20, unique=True)),
                ('short_name', models.CharField(max_length=1, unique=True)),
                ('slug', models.SlugField(help_text='A lable for URL config', max_length=20, unique=True)),
            ],
            options={
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(help_text='A lable for URL config', max_length=20, unique=True)),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook_app.Class')),
            ],
            options={
                'ordering': ['_class', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(help_text='A label for URL config', max_length=100, unique=True)),
            ],
            options={
                'ordering': ['text'],
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(help_text='A lable for URL config', max_length=20, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(help_text='A label for URL config', max_length=100, unique=True)),
            ],
            options={
                'ordering': ['text'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(help_text='A lable for URL config', max_length=20, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, unique=True)),
                ('short_name', models.CharField(max_length=10, unique=True)),
                ('slug', models.SlugField(help_text='A lable for URL config', max_length=20, unique=True)),
                ('link', models.URLField(max_length=255)),
                ('public', models.BooleanField()),
            ],
            options={
                'ordering': ['short_name'],
            },
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(help_text='A lable for URL config', max_length=100, unique=True)),
                ('text', models.TextField()),
                ('concentration', models.BooleanField()),
                ('ritual', models.BooleanField()),
                ('cast_time_misc', models.CharField(max_length=100)),
                ('component_misc', models.CharField(max_length=100)),
                ('range_misc', models.CharField(max_length=100)),
                ('_class', models.ManyToManyField(related_name='_class', to='spellbook_app.Class')),
                ('_range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook_app.Range')),
                ('casting_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook_app.CastingTime')),
                ('component', models.ManyToManyField(related_name='component', to='spellbook_app.Component')),
                ('domain', models.ManyToManyField(blank=True, related_name='domain', to='spellbook_app.Domain')),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook_app.Duration')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook_app.Level')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook_app.School')),
            ],
        ),
        migrations.CreateModel(
            name='SpellSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=20)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook_app.Source')),
                ('spell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook_app.Spell')),
            ],
            options={
                'ordering': ['source', 'spell'],
            },
        ),
        migrations.AddField(
            model_name='spell',
            name='source',
            field=models.ManyToManyField(related_name='source', through='spellbook_app.SpellSource', to='spellbook_app.Source'),
        ),
    ]

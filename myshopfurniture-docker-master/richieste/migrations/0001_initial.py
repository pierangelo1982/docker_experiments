# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-28 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Richiesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Titolo')),
                ('cognome', models.CharField(max_length=100, verbose_name='cognome')),
                ('indirizzo', models.CharField(blank=True, max_length=100, null=True, verbose_name='indirizzo')),
                ('civico', models.CharField(blank=True, max_length=100, null=True, verbose_name='numero civico')),
                ('cap', models.CharField(blank=True, max_length=100, null=True, verbose_name='cap')),
                ('citta', models.CharField(blank=True, max_length=100, null=True, verbose_name='citta')),
                ('telefono', models.CharField(blank=True, max_length=100, null=True, verbose_name='telefono')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('oggetto', models.CharField(blank=True, max_length=100, null=True, verbose_name='oggetto')),
                ('descrizione', models.TextField(blank=True, null=True, verbose_name='Descrizione')),
                ('allegato', models.FileField(blank=True, null=True, upload_to='richieste_allegati')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name_plural': 'Richiesta',
            },
        ),
    ]
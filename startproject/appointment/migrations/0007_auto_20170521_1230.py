# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_appoint_acm_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='place',
            field=models.CharField(default=1, max_length=32, verbose_name='地点'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='time',
            field=models.CharField(default=1, max_length=32, verbose_name='时间'),
            preserve_default=False,
        ),
    ]

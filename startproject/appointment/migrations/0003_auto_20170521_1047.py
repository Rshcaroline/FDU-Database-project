# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20170516_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='start_time',
            field=models.DateField(verbose_name='开始时间'),
        ),
    ]

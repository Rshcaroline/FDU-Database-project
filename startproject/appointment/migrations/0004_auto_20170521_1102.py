# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20170521_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoint',
            name='x_id',
        ),
        migrations.RemoveField(
            model_name='appoint',
            name='x_type',
        ),
        migrations.AddField(
            model_name='appoint',
            name='acm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appointment.Acm', verbose_name='竞赛生'),
            preserve_default=False,
        ),
    ]

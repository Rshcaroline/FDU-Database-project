# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0008_remove_appoint_acm_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoint_acm',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='邮箱'),
            preserve_default=False,
        ),
    ]

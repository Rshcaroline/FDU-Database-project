# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]

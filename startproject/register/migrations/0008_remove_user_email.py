# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_remove_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]

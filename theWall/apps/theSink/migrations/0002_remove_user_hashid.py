# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-19 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theSink', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hashId',
        ),
    ]

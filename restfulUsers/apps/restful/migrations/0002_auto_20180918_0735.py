# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-18 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.TimeField(auto_now=True),
        ),
    ]

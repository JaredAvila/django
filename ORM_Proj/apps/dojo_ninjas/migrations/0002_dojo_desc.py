# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-17 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='description', max_length=1000),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-22 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180922_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='name',
            field=models.CharField(blank=True, default='None', max_length=255),
        ),
    ]

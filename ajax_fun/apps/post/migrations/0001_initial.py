# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-23 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
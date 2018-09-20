# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-19 23:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theSink', '0004_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='message_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='recipe_id',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='theSink.Recipe'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
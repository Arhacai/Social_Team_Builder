# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-23 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20180822_1857'),
        ('projects', '0015_auto_20180823_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='related_skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Skill'),
        ),
    ]
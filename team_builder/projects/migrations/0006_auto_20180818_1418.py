# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-18 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180818_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='applicantions',
            new_name='applications',
        ),
    ]
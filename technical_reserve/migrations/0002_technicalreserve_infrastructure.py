# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('underground_box', '0002_auto_20170922_0028'),
        ('technical_reserve', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicalreserve',
            name='infrastructure',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='underground_box.UndergroundBox'),
            preserve_default=False,
        ),
    ]

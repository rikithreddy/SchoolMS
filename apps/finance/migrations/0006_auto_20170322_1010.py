# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170321_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(max_length=50),
        ),
    ]

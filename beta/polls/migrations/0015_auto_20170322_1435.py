# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20170322_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feestruct',
            name='numberTerms',
            field=models.IntegerField(default=3),
        ),
    ]

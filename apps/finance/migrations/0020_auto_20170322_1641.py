# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20170322_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='salary',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

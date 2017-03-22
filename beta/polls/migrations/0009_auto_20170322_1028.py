# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 04:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20170322_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='id',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='staffID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Staff'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staffID',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]

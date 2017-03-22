# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170315_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='joinDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], max_length=50),
        ),
    ]

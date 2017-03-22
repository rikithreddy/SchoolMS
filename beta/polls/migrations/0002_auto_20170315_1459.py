# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addrID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cID', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='roleID',
        ),
        migrations.AddField(
            model_name='staff',
            name='joinDate',
            field=models.CharField(default=b'-', max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='position',
            field=models.CharField(default=b'position', max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staffID',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='staff',
            name='addrID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Address'),
        ),
        migrations.AddField(
            model_name='staff',
            name='cID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Contact'),
        ),
    ]
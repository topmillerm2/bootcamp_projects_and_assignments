# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-17 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
1
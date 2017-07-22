# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-17 00:00
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('expenses', '0005_auto_20170714_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('expenses', '0008_remove_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

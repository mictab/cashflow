# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0012_auto_20170823_0307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetline',
            name='cost_centre',
        ),
        migrations.RemoveField(
            model_name='costcentre',
            name='committee',
        ),
        migrations.RemoveField(
            model_name='expensepart',
            name='budget_line',
        ),
        migrations.AddField(
            model_name='expensepart',
            name='budget_line_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expensepart',
            name='budget_line_name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='expensepart',
            name='committee_name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='expensepart',
            name='cost_centre_name',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='BudgetLine',
        ),
        migrations.DeleteModel(
            name='Committee',
        ),
        migrations.DeleteModel(
            name='CostCentre',
        ),
    ]

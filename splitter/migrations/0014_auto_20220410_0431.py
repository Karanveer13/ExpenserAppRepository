# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-10 04:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0013_auto_20220410_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense_splitter',
            name='e_splitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Expense_Group_Friend', to='splitter.Group_Friend'),
        ),
        migrations.AlterField(
            model_name='expense_splitter',
            name='expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Expense_name', to='splitter.Expense'),
        ),
    ]

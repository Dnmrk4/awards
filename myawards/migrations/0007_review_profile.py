# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-05 04:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myawards', '0006_review_overall_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myawards.Profile'),
            preserve_default=False,
        ),
    ]

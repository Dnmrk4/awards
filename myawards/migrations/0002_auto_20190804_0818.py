# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-04 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myawards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profilepic',
            new_name='profile_photo',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 20:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
    ]

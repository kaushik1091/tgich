# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151218184805 on 2015-12-21 06:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_auto_20151221_0610'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='moviecrew',
            unique_together=set([('movie', 'artist', 'role', 'character_name')]),
        ),
    ]

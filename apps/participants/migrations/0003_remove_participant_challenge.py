# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("participants", "0002_participantteam_participantteammember")
    ]

    operations = [
        migrations.RemoveField(model_name="participant", name="challenge")
    ]

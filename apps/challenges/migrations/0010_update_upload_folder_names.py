# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-08 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0009_challengephase_is_public")]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="evaluation_script",
            field=models.FileField(
                default=False, upload_to="evaluation_scripts"
            ),
        ),
        migrations.AlterField(
            model_name="challengephase",
            name="test_annotation",
            field=models.FileField(upload_to="test_annotations"),
        ),
    ]

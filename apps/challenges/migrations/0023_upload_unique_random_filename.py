# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-16 17:16
from __future__ import unicode_literals

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0022_challengephase_dataset_split")]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="evaluation_script",
            field=models.FileField(
                default=False,
                upload_to=base.utils.RandomFileName("evaluation_scripts"),
            ),
        ),
        migrations.AlterField(
            model_name="challengephase",
            name="test_annotation",
            field=models.FileField(
                upload_to=base.utils.RandomFileName("test_annotations")
            ),
        ),
    ]

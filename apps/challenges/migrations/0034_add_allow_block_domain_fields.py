# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-30 10:24
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0033_delete_unique_constraint_from_datasetsplit_table")
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="allowed_email_domains",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=50),
                blank=True,
                default=[],
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="blocked_email_domains",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=50),
                blank=True,
                default=[],
                size=None,
            ),
        ),
    ]

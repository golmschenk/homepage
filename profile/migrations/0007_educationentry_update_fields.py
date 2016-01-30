# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0006_educationentry_graduation_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educationentry',
            old_name='text',
            new_name='additional_information',
        ),
        migrations.AddField(
            model_name='educationentry',
            name='degree',
            field=models.TextField(default=''),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0012_project_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachingentry',
            name='position',
            field=models.TextField(blank=True),
        ),
    ]

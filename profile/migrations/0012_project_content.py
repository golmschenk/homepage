# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0011_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='url_to_code',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='url_to_site',
            field=models.URLField(default=''),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_essay_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180628_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='头像'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-30 08:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='produts',
            new_name='products',
        ),
    ]

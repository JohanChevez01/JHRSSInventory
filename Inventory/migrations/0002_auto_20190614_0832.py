# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-14 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventarioequipo',
            old_name='codigo_Equipo',
            new_name='codigo_equipo',
        ),
        migrations.AlterField(
            model_name='otroinventario',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]

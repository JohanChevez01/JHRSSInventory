# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_auto_20190619_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='otroinventario',
            name='estado_equipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inventory.EstadoEquipo'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Censor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GWCredentials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('GWID', models.CharField(max_length=9)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField(max_length=255)),
                ('gender', models.BooleanField(choices=[(True, b'male'), (False, b'female')])),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.BigIntegerField()),
            ],
        ),
    ]

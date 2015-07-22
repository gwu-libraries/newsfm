# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0003_auto_20150708_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='collection_id',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='group',
        ),
        migrations.RemoveField(
            model_name='seed',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='seed',
            name='group',
        ),
        migrations.RemoveField(
            model_name='seed',
            name='seed_id',
        ),
        migrations.RemoveField(
            model_name='seed',
            name='seed_set',
        ),
        migrations.RemoveField(
            model_name='seedset',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='seedset',
            name='group',
        ),
        migrations.RemoveField(
            model_name='seedset',
            name='seed_set_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AddField(
            model_name='collection',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seed',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seedset',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='group_id',
            field=models.AutoField(default=b'1', serialize=False, primary_key=True),
        ),
    ]

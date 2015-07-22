# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0002_collection_group_home_seed_seedset_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('log_id', models.AutoField(serialize=False, primary_key=True)),
                ('log', models.TextField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='collection',
            name='id',
        ),
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.RemoveField(
            model_name='seed',
            name='id',
        ),
        migrations.RemoveField(
            model_name='seedset',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='collection',
            name='collection_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='group',
            field=models.ForeignKey(default=1, to='social_app.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='group_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seed',
            name='collection',
            field=models.ForeignKey(default=1, to='social_app.Collection'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seed',
            name='group',
            field=models.ForeignKey(default=1, to='social_app.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seed',
            name='seed_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seed',
            name='seed_set',
            field=models.ForeignKey(default=1, to='social_app.SeedSet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seedset',
            name='collection',
            field=models.ForeignKey(default=1, to='social_app.Collection'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seedset',
            name='group',
            field=models.ForeignKey(default=1, to='social_app.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seedset',
            name='seed_set_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]

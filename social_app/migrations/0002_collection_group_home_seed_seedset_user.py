# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection_name', models.CharField(max_length=25)),
                ('collection_desc', models.TextField(max_length=255)),
                ('group_name', models.CharField(max_length=25)),
                ('collection_method', models.CharField(default=b'Harvest', max_length=20, choices=[(b'Harvest', b'Harvest'), (b'Full Harvest', b'Full Harvest'), (b'Live Stream', b'Live Stream'), (b'Sample Stream', b'Sample Stream')])),
                ('collection_schedule', models.CharField(default=b'Monthly', max_length=20, choices=[(b'Daily', b'Daily'), (b'Weekly', b'Weekly'), (b'Bi-Weekly', b'Bi-Weekly'), (b'Monthly', b'Monthly')])),
                ('collection_last_updated', models.DateTimeField()),
                ('collection_status', models.BooleanField(choices=[(True, b'inactive'), (False, b'active')])),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=25)),
                ('group_desc', models.TextField(max_length=255)),
                ('group_last_updated', models.DateTimeField()),
                ('group_status', models.BooleanField(choices=[(True, b'inactive'), (False, b'active')])),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection_name', models.CharField(max_length=50)),
                ('collection_desc', models.TextField(max_length=255)),
                ('collection_count', models.IntegerField()),
                ('collection_type', models.CharField(default=b'Harvest', max_length=50, choices=[(b'Live Stream', b'Live Stream'), (b'Sample Stream', b'Sample Stream'), (b'Full Harvest', b'Full Harvest'), (b'Harvest', b'Harvest')])),
                ('collection_last_updated', models.DateField()),
                ('collection_part_of_group', models.CharField(max_length=50)),
                ('collection_status', models.BooleanField(choices=[(True, b'disabled'), (False, b'enabled')])),
                ('seed_set_name', models.CharField(max_length=50)),
                ('seed_set_desc', models.TextField(max_length=255)),
                ('seed_set_type', models.CharField(default=b'Twitter_Accounts', max_length=50, choices=[(b'Twitter_Handles', b'Twitter_Handles'), (b'Twitter_Accounts', b'Twitter_Accounts'), (b'Twitter_Searches', b'Twitter_Searches'), (b'Flickr_Handles', b'Flickr_Handles'), (b'Flickr_Accounts', b'Flickr_Accounts'), (b'Flickr_Images', b'Flickr_Images'), (b'Tumblr_Handles', b'Tumblr_Handles'), (b'Tumblr_Accounts', b'Tumblr_Accounts'), (b'Tumblr_Blogs', b'Tumblr_Blogs')])),
                ('seed_set_status', models.BooleanField(choices=[(True, b'disabled'), (False, b'enabled')])),
                ('seed_set_count', models.IntegerField()),
                ('seed_set_last_updated', models.DateField()),
                ('seed_name', models.CharField(max_length=50)),
                ('seed_desc', models.TextField(max_length=255)),
                ('seed_status', models.BooleanField(choices=[(True, b'disabled'), (False, b'enabled')])),
                ('seed_count', models.IntegerField()),
                ('seed_last_updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seed_name', models.CharField(max_length=25)),
                ('seed_desc', models.TextField(max_length=255)),
                ('collection_method', models.CharField(default=b'Harvest', max_length=20, choices=[(b'Harvest', b'Harvest'), (b'Full Harvest', b'Full Harvest'), (b'Live Stream', b'Live Stream'), (b'Sample Stream', b'Sample Stream')])),
                ('collection_schedule', models.CharField(default=b'Monthly', max_length=20, choices=[(b'Daily', b'Daily'), (b'Weekly', b'Weekly'), (b'Bi-Weekly', b'Bi-Weekly'), (b'Monthly', b'Monthly')])),
                ('seed_last_updated', models.DateTimeField()),
                ('seed_status', models.BooleanField(choices=[(True, b'inactive'), (False, b'active')])),
            ],
        ),
        migrations.CreateModel(
            name='SeedSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seed_set_name', models.CharField(max_length=25)),
                ('seed_set_desc', models.TextField(max_length=255)),
                ('seed_set_type', models.CharField(default=b'Twitter Account', max_length=20, choices=[(b'Twitter Account', b'Twitter Account'), (b'Twitter Hashtag', b'Twitter Hashtag'), (b'Twitter Search', b'Twitter Search'), (b'Flickr Account', b'Flickr Account'), (b'Flickr Search', b'Flickr Search'), (b'Flickr Tag', b'Flickr Tag'), (b'Tumblr Account', b'Tumblr Account'), (b'Tumblr Search', b'Tumblr Search'), (b'Tumblr Blog', b'Tumblr Blog')])),
                ('collection_method', models.CharField(default=b'Harvest', max_length=20, choices=[(b'Harvest', b'Harvest'), (b'Full Harvest', b'Full Harvest'), (b'Live Stream', b'Live Stream'), (b'Sample Stream', b'Sample Stream')])),
                ('collection_schedule', models.CharField(default=b'Monthly', max_length=20, choices=[(b'Daily', b'Daily'), (b'Weekly', b'Weekly'), (b'Bi-Weekly', b'Bi-Weekly'), (b'Monthly', b'Monthly')])),
                ('seed_set_last_updated', models.DateTimeField()),
                ('seed_set_status', models.BooleanField(choices=[(True, b'inactive'), (False, b'active')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=25)),
                ('bio', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.BigIntegerField()),
            ],
        ),
    ]

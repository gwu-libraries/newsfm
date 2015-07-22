from django.contrib import admin as a
from social_app import models as m
# Register your models here.

"""
class GWCredentials(a.ModelAdmin):
    fields = ('GWID', 'password')
    list_display = ['GWID', 'password']
    list_filter = ['GWID']
    search_fields = ['GWID']

a.site.register(m.GWCredentials, GWCredentials)


class Profile(a.ModelAdmin):
    fields = ('name', 'bio', 'gender', 'dob', 'email', 'contact')
    list_display = ['name', 'bio', 'gender', 'dob', 'email', 'contact']
    list_filter = ['name', 'bio', 'gender', 'dob', 'email', 'contact']
    search_fields = ['name', 'bio', 'gender', 'dob', 'email', 'contact']

a.site.register(m.Profile, Profile)"""


class Group(a.ModelAdmin):
    fields = ('group_id', 'group_name', 'group_desc', 'group_last_updated',
              'group_status')
    list_display = ['group_id', 'group_name', 'group_desc',
                    'group_last_updated', 'group_status']
    list_filter = ['group_id', 'group_name', 'group_desc',
                   'group_last_updated', 'group_status']
    search_fields = ['group_id', 'group_name', 'group_desc',
                     'group_last_updated', 'group_status']

a.site.register(m.Group, Group)


class Collection(a.ModelAdmin):
    fields = ('collection_name', 'collection_desc', 'group_name',
              'collection_method', 'collection_schedule',
              'collection_last_updated', 'collection_status')
    list_display = ['collection_name', 'collection_desc', 'group_name',
                    'collection_method', 'collection_schedule',
                    'collection_last_updated', 'collection_status']
    # list_filter = ['collection_name', 'collection_desc', 'group_name']
    search_fields = ['collection_name', 'collection_desc', 'group_name'
                     'collection_method', 'collection_schedule',
                     'collection_last_updated', 'collection_status']

a.site.register(m.Collection, Collection)


class User(a.ModelAdmin):
    fields = ('user_name', 'bio', 'email', 'contact')
    list_display = ['user_name', 'bio', 'email', 'contact']
    search_fields = ['user_name', 'bio', 'email', 'contact']

a.site.register(m.User, User)


class SeedSet(a.ModelAdmin):
    fields = ('seed_set_name', 'seed_set_desc', 'seed_set_type',
              'collection_method', 'collection_schedule',
              'seed_set_last_updated', 'seed_set_status')
    list_display = ['seed_set_name', 'seed_set_desc', 'seed_set_type',
                    'collection_method', 'collection_schedule',
                    'seed_set_last_updated', 'seed_set_status']
    search_fields = ['seed_set_name', 'seed_set_desc', 'seed_set_type',
                     'collection_method', 'collection_schedule',
                     'seed_set_last_updated', 'seed_set_status']

a.site.register(m.SeedSet, SeedSet)


class Seed(a.ModelAdmin):
    fields = ('seed_name', 'seed_desc', 'collection_method',
              'collection_schedule', 'seed_last_updated', 'seed_status')
    list_display = ['seed_name', 'seed_desc', 'collection_method',
                    'collection_schedule', 'seed_last_updated', 'seed_status']
    search_fields = ['seed_name', 'seed_desc', 'collection_method',
                     'collection_schedule', 'seed_last_updated', 'seed_status']

a.site.register(m.Seed, Seed)

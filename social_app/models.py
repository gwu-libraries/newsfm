from django.db import models as m


# Create your models here.


class Group(m.Model):
    group_id = m.AutoField(primary_key=True, default='1')
    group_name = m.CharField(max_length=25)
    group_desc = m.TextField(max_length=255)
    group_last_updated = m.DateTimeField()
    group_status = m.BooleanField(choices=((True, 'inactive'),
                                           (False, 'active')))


class Collection(m.Model):
    # collection_id = m.AutoField(primary_key=True)
    # group = m.ForeignKey(Group)
    collection_name = m.CharField(max_length=25)
    collection_desc = m.TextField(max_length=255)
    # group_name = m.OneToOneField(group_name, collection_id)
    group_name = m.CharField(max_length=25)
    methods = (
        ('Harvest', 'Harvest'),
        ('Full Harvest', 'Full Harvest'),
        ('Live Stream', 'Live Stream'),
        ('Sample Stream', 'Sample Stream'),
    )
    # methods = get it from database
    collection_method = m.CharField(max_length=20, choices=methods,
                                    default='Harvest')
    schedule = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Bi-Weekly', 'Bi-Weekly'),
        ('Monthly', 'Monthly'),
    )
    # schedule = get it from database
    collection_schedule = m.CharField(max_length=20, choices=schedule,
                                      default='Monthly')
    collection_last_updated = m.DateTimeField()
    collection_status = m.BooleanField(choices=((True, 'inactive'),
                                                (False, 'active')))


class User(m.Model):
    # user_id = m.AutoField(primary_key=True)
    user_name = m.CharField(max_length=25)
    # user_name = session.user.name
    # gwid = session.user
    bio = m.TextField(max_length=255)
    email = m.EmailField()
    contact = m.BigIntegerField()


class SeedSet(m.Model):
    # seed_set_id = m.AutoField(primary_key=True)
    # collection = m.ForeignKey(Collection)
    # group = m.ForeignKey(Group)
    seed_set_name = m.CharField(max_length=25)
    seed_set_desc = m.TextField(max_length=255)
    # collection_name = OnetoOneField(collection_name, seed_set_id)
    # group_name = OnetoOneField(group_name, seed_set_id)
    types = (
        ('Twitter Account', 'Twitter Account'),
        ('Twitter Hashtag', 'Twitter Hashtag'),
        ('Twitter Search', 'Twitter Search'),
        ('Flickr Account', 'Flickr Account'),
        ('Flickr Search', 'Flickr Search'),
        ('Flickr Tag', 'Flickr Tag'),
        ('Tumblr Account', 'Tumblr Account'),
        ('Tumblr Search', 'Tumblr Search'),
        ('Tumblr Blog', 'Tumblr Blog'),
    )
    # types = get it from database
    seed_set_type = m.CharField(max_length=20, choices=types,
                                default='Twitter Account')
    methods = (
        ('Harvest', 'Harvest'),
        ('Full Harvest', 'Full Harvest'),
        ('Live Stream', 'Live Stream'),
        ('Sample Stream', 'Sample Stream'),
    )
    # methods = get it from database
    collection_method = m.CharField(max_length=20, choices=methods,
                                    default='Harvest')
    schedule = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Bi-Weekly', 'Bi-Weekly'),
        ('Monthly', 'Monthly'),
    )
    # schedule = get it from database
    collection_schedule = m.CharField(max_length=20, choices=schedule,
                                      default='Monthly')
    seed_set_last_updated = m.DateTimeField()
    seed_set_status = m.BooleanField(choices=((True, 'inactive'),
                                              (False, 'active')))


class Seed(m.Model):
    # seed_id = m.AutoField(primary_key=True)
    # seed_set = m.ForeignKey(SeedSet)
    # collection = m.ForeignKey(Collection)
    # group = m.ForeignKey(Group)
    seed_name = m.CharField(max_length=25)
    seed_desc = m.TextField(max_length=255)
    # collection_name = get it from database
    # group_name = get it from database
    methods = (
        ('Harvest', 'Harvest'),
        ('Full Harvest', 'Full Harvest'),
        ('Live Stream', 'Live Stream'),
        ('Sample Stream', 'Sample Stream'),
    )
    # methods = get it from database
    collection_method = m.CharField(max_length=20, choices=methods,
                                    default='Harvest')
    schedule = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Bi-Weekly', 'Bi-Weekly'),
        ('Monthly', 'Monthly'),
    )
    # schedule = get it from database
    collection_schedule = m.CharField(max_length=20, choices=schedule,
                                      default='Monthly')
    seed_last_updated = m.DateTimeField()
    seed_status = m.BooleanField(choices=((True, 'inactive'),
                                          (False, 'active')))


class Log(m.Model):
    log_id = m.AutoField(primary_key=True)
    log = m.TextField(max_length=255)

""" Not Required Models
class GWCredentials(m.Model):
    GWID = m.CharField(max_length=9)
    password = m.CharField(max_length=50)


class Profile(m.Model):
    name = m.CharField(max_length=50)
    bio = m.TextField(max_length=255)
    gender = m.BooleanField(choices=((True, 'male'), (False, 'female')))
    dob = m.DateField()
    email = m.EmailField()
    contact = m.BigIntegerField()
"""


class Home(m.Model):
    collection_name = m.CharField(max_length=50)
    collection_desc = m.TextField(max_length=255)
    collection_count = m.IntegerField()
    LiveStream = 'Live Stream'
    SampleStream = 'Sample Stream'
    FullHarvest = 'Full Harvest'
    Harvest = 'Harvest'
    types = (
        (LiveStream, 'Live Stream'),
        (SampleStream, 'Sample Stream'),
        (FullHarvest, 'Full Harvest'),
        (Harvest, 'Harvest'),
    )
    collection_type = m.CharField(max_length=50, choices=types, default=Harvest)

    collection_last_updated = m.DateField()
    collection_part_of_group = m.CharField(max_length=50)
    collection_status = m.BooleanField(choices=((True, 'disabled'),
                                                (False, 'enabled')))
    seed_set_name = m.CharField(max_length=50)
    seed_set_desc = m.TextField(max_length=255)
    TwitterHandles = 'Twitter_Handles'
    TwitterAccounts = 'Twitter_Accounts'
    TwitterSearches = 'Twitter_Searches'
    FlickrHandles = 'Flickr_Handles'
    FlickrAccounts = 'Flickr_Accounts'
    FlickrImages = 'Flickr_Images'
    TumblrHandles = 'Tumblr_Handles'
    TumblrAccounts = 'Tumblr_Accounts'
    TumblrBlogs = 'Tumblr_Blogs'
    seed_types = (
        (TwitterHandles, 'Twitter_Handles'),
        (TwitterAccounts, 'Twitter_Accounts'),
        (TwitterSearches, 'Twitter_Searches'),
        (FlickrHandles, 'Flickr_Handles'),
        (FlickrAccounts, 'Flickr_Accounts'),
        (FlickrImages, 'Flickr_Images'),
        (TumblrHandles, 'Tumblr_Handles'),
        (TumblrAccounts, 'Tumblr_Accounts'),
        (TumblrBlogs, 'Tumblr_Blogs'),
    )
    seed_set_type = m.CharField(max_length=50, choices=seed_types,
                                default=TwitterAccounts)

    seed_set_status = m.BooleanField(choices=((True, 'disabled'),
                                              (False, 'enabled')))
    seed_set_count = m.IntegerField()
    seed_set_last_updated = m.DateField()
    seed_name = m.CharField(max_length=50)
    seed_desc = m.TextField(max_length=255)
    seed_status = m.BooleanField(choices=((True, 'disabled'),
                                          (False, 'enabled')))
    seed_count = m.IntegerField()
    seed_last_updated = m.DateField()

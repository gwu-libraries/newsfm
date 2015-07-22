from django import forms as f
from social_app.models import  Home, Log
from social_app.models import Collection, Group, User, SeedSet, Seed
# from django.contrib.admin import widgets
# from django.forms.extras.widgets import SelectDateWidget

""" Not Required Form
class GWCredentialsForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GWCredentialsForm, self).__init__(*args, **kwargs)
        self.fields['GWID'].required = True
        self.fields['password'].required = True

    class Meta:
        model = GWCredentials
        widgets = {
            'password': f.PasswordInput(),
        }
        fields = '__all__'
"""


class LogForm(f.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LogForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Log
        fields = '__all__'

""" Not Required Form
class ProfileForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['bio'].required = True
        self.fields['gender'].required = True
        # gender = f.TypedChoiceField(choices=(True, 'male'), (False, 'female'),
        #                                 widget=RadioSelect, coerce=bool)
        self.fields['dob'].required = True
        self.fields['email'].required = True
        self.fields['contact'].required = True

    class Meta:
        model = Profile
        fields = '__all__'
"""


class HomeForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HomeForm, self).__init__(*args, **kwargs)
        self.fields['collection_name'].required = True
        self.fields['collection_desc'].required = True
        self.fields['collection_type'].required = True
        self.fields['collection_count'].required = True
        self.fields['collection_last_updated'].required = True
        self.fields['collection_part_of_group'].required = True
        self.fields['collection_status'].required = True
        self.fields['seed_set_name'].required = True
        self.fields['seed_set_desc'].required = True
        self.fields['seed_set_type'].required = True
        self.fields['seed_set_count'].required = True
        self.fields['seed_set_last_updated'].required = True
        self.fields['seed_set_status'].required = True
        self.fields['seed_name'].required = True
        self.fields['seed_desc'].required = True
        self.fields['seed_count'].required = True
        self.fields['seed_last_updated'].required = True
        self.fields['seed_status'].required = True

    class Meta:
        model = Home
        fields = '__all__'


class HomeReadOnlyForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HomeReadOnlyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = self.fields[field].label
            # if isinstance(self.fields[field].widget, Select):
            # self.fields[field].widget.attrs['disabled'] = 'disabled'
            # else:
            self.fields[field].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Home
        fields = '__all__'


class CollectionForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Collection
        fields = '__all__'


class CollectionReadOnlyForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CollectionReadOnlyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Collection
        fields = '__all__'


class GroupForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['group_id'].is_hidden = True

    class Meta:
        model = Group
        fields = '__all__'


class GroupReadOnlyForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GroupReadOnlyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Group
        fields = '__all__'


class UserForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = '__all__'


class UserReadOnlyForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserReadOnlyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = User
        fields = '__all__'


class SeedSetForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SeedSetForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SeedSet
        fields = '__all__'


class SeedSetReadOnlyForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SeedSetReadOnlyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = SeedSet
        fields = '__all__'


class SeedForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SeedForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Seed
        fields = '__all__'


class SeedReadOnlyForm(f.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SeedReadOnlyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Seed
        fields = '__all__'

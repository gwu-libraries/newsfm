from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required
# from social_app.forms import GWCredentialsForm, ProfileForm, HomeReadOnlyForm
from social_app.forms import CollectionReadOnlyForm, CollectionForm
from social_app.forms import GroupForm, GroupReadOnlyForm
from social_app.forms import SeedSetReadOnlyForm, SeedSetForm
from social_app.forms import UserForm, UserReadOnlyForm
from social_app.forms import SeedReadOnlyForm, SeedForm
from social_app.models import User, Group, Collection, Seed, SeedSet
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic.list import ListView
from social.actions import do_complete
from social.apps.django_app.utils import strategy
from social.apps.django_app.views import _do_login
# from django.contrib.auth import logout
# from django.template.context import RequestContext


# It Gives the Home Screen which is Displaying all permissions that the user is
# having and the login links to different social accounts
def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html')


""" Not required views
@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')
"""


def logout(request):
    auth_logout(request)
    return redirect('/')

""" Not Required View
def gwhome(request):
    if request.method == 'POST':
        form = HomeReadOnlyForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            if request.user.is_authenticated():
                return redirect('home.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form = HomeReadOnlyForm()
        return render(request, 'gwhome.html', {'form': form})
"""


def user(request):
    if request.method == 'POST':
        form = UserReadOnlyForm(request.POST)
        # susers = User.objects.all()
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            if request.user.is_authenticated():
                return redirect('home.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form = UserReadOnlyForm()
        return render(request, 'user.html', {'form': form})


def useredit(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            if request.user.is_authenticated():
                return redirect('home.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form = UserForm()
    return render(request, 'useredit.html', {'form': form})


class UserListView(ListView):

    model = User

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class SeedListView(ListView):

    model = Seed

    def get_context_data(self, **kwargs):
        context = super(SeedListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class SeedSetListView(ListView):

    model = SeedSet

    def get_context_data(self, **kwargs):
        context = super(SeedSetListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CollectionListView(ListView):

    model = Collection

    def get_context_data(self, **kwargs):
        context = super(CollectionListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class GroupListView(ListView):

    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def seed(request):
    if request.method == 'POST':
        form = SeedReadOnlyForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            if request.user.is_authenticated():
                return redirect('home.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form = SeedReadOnlyForm()
    return render(request, 'seed.html', {'form': form})


def seededit(request):
    if request.method == 'POST':
        form = SeedForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            if request.user.is_authenticated():
                return redirect('home.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form = SeedForm()
    return render(request, 'seededit.html', {'form': form})


def homeview(request):
    if request.method == 'POST':
        form1 = CollectionReadOnlyForm(request.POST)
        form2 = SeedSetReadOnlyForm(request.POST)
        form3 = SeedReadOnlyForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            print 'all validation passed'
            model_instance1 = form1.save(commit=False)
            form2.cleaned_data['model_instance1'] = model_instance1
            model_instance2 = form2.save(commit=False)
            form3.cleaned_data['model_instance1'] = model_instance1
            model_instance3 = form3.save(commit=False)
            model_instance1.save()
            model_instance2.save()
            model_instance3.save()
            if request.user.is_authenticated():
                return redirect('gwhome.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form1 = CollectionReadOnlyForm()
        form2 = SeedSetReadOnlyForm()
        form3 = SeedReadOnlyForm()
    return render(request, 'homeview.html', {
        'form1': form1,
        'form2': form2,
        'form3': form3,
    })


def group(request):
    if request.method == 'POST':
        form1 = GroupReadOnlyForm(request.POST)
        form2 = CollectionReadOnlyForm(request.POST)
        form3 = SeedSetReadOnlyForm(request.POST)
        form4 = SeedReadOnlyForm(request.POST)
        if (form1.is_valid() and form2.is_valid()
            and form3.is_valid() and form4.is_valid()):
            print 'all validation passed'
            model_instance1 = form1.save(commit=False)
            form2.cleaned_data['model_instance1'] = model_instance1
            model_instance2 = form2.save(commit=False)
            form3.cleaned_data['model_instance1'] = model_instance1
            model_instance3 = form3.save(commit=False)
            form4.cleaned_data['model_instance1'] = model_instance1
            model_instance4 = form4.save(commit=False)
            model_instance1.save()
            model_instance2.save()
            model_instance3.save()
            model_instance4.save()
            if request.user.is_authenticated():
                return redirect('gwhome.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form1 = GroupReadOnlyForm()
        form2 = CollectionReadOnlyForm()
        form3 = SeedSetReadOnlyForm()
        form4 = SeedReadOnlyForm()
    return render(request, 'group.html', {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
    })


def groupedit(request):
    if request.method == 'POST':
        form1 = GroupForm(request.POST)
        form2 = CollectionForm(request.POST)
        form3 = SeedSetForm(request.POST)
        form4 = SeedForm(request.POST)
        if (form1.is_valid() and form2.is_valid()
            and form3.is_valid() and form4.is_valid()):
            print 'all validation passed'
            model_instance1 = form1.save(commit=False)
            form2.cleaned_data['model_instance1'] = model_instance1
            model_instance2 = form2.save(commit=False)
            form3.cleaned_data['model_instance1'] = model_instance1
            model_instance3 = form3.save(commit=False)
            form4.cleaned_data['model_instance1'] = model_instance1
            model_instance4 = form4.save(commit=False)
            model_instance1.save()
            model_instance2.save()
            model_instance3.save()
            model_instance4.save()
            if request.user.is_authenticated():
                return redirect('group.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form1 = GroupForm()
        form2 = CollectionForm()
        form3 = SeedSetForm()
        form4 = SeedForm()
    return render(request, 'groupedit.html', {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
    })


def collection(request):
    if request.method == 'POST':
        form1 = CollectionReadOnlyForm(request.POST)
        form2 = SeedSetReadOnlyForm(request.POST)
        form3 = SeedReadOnlyForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            print 'all validation passed'
            model_instance1 = form1.save(commit=False)
            form2.cleaned_data['model_instance1'] = model_instance1
            model_instance2 = form2.save(commit=False)
            form3.cleaned_data['model_instance1'] = model_instance1
            model_instance3 = form3.save(commit=False)
            model_instance1.save()
            model_instance2.save()
            model_instance3.save()
            if request.user.is_authenticated():
                return redirect('gwhome.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form1 = CollectionReadOnlyForm()
        form2 = SeedSetReadOnlyForm()
        form3 = SeedReadOnlyForm()
    return render(request, 'homeview.html', {
        'form1': form1,
        'form2': form2,
        'form3': form3,
    })


def collectionedit(request):
    if request.method == 'POST':
        form1 = CollectionForm(request.POST)
        form2 = SeedSetForm(request.POST)
        form3 = SeedForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            print 'all validation passed'
            model_instance1 = form1.save(commit=False)
            form2.cleaned_data['model_instance1'] = model_instance1
            model_instance2 = form2.save(commit=False)
            form3.cleaned_data['model_instance1'] = model_instance1
            model_instance3 = form3.save(commit=False)
            model_instance1.save()
            model_instance2.save()
            model_instance3.save()
            if request.user.is_authenticated():
                return redirect('gwhome.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form1 = CollectionForm()
        form2 = SeedSetForm()
        form3 = SeedForm()
    return render(request, 'homeview.html', {
        'form1': form1,
        'form2': form2,
        'form3': form3,
    })


def seedsetedit(request):
    if request.method == 'POST':
        form1 = SeedSetForm(request.POST)
        form2 = SeedForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print 'all validation passed'
            model_instance1 = form1.save(commit=False)
            form2.cleaned_data['model_instance1'] = model_instance1
            model_instance2 = form2.save(commit=False)
            model_instance1.save()
            model_instance2.save()
            if request.user.is_authenticated():
                return redirect('gwhome.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form1 = SeedSetForm()
        form2 = SeedForm()
    return render(request, 'seedsetedit.html', {
        'form1': form1,
        'form2': form2,
    })


def seedset(request):
    if request.method == 'POST':
        form1 = SeedSetReadOnlyForm(request.POST)
        form2 = SeedReadOnlyForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print 'all validation passed'
            model_instance1 = form1.save(commit=False)
            form2.cleaned_data['model_instance1'] = model_instance1
            model_instance2 = form2.save(commit=False)
            model_instance1.save()
            model_instance2.save()
            if request.user.is_authenticated():
                return redirect('gwhome.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form1 = SeedSetReadOnlyForm()
        form2 = SeedReadOnlyForm()
    return render(request, 'seedset.html', {
        'form1': form1,
        'form2': form2,
    })

""" Not Required View
def gwlogin(request):
    if request.method == 'POST':
        form = GWCredentialsForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            if request.user.is_authenticated():
                return redirect('home.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form = GWCredentialsForm()
    return render(request, 'gwlogin.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            if request.user.is_authenticated():
                return redirect('home.html')
            else:
                return HttpResponse('Invalid User')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})
"""


# @csrf_exempt
@strategy('social:complete')
def complete(request, backend, *args, **kwargs):
    """Override this method so we can force user to be logged out."""
    return do_complete(request.social_strategy, _do_login, user=None,
                       redirect_name='home', *args, **kwargs)


def social_user(backend, uid, user=None, *args, **kwargs):
    '''OVERRIDED: It will logout the current user
    instead of raise an exception '''

    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            logout(backend.strategy.request)
            # msg = 'This {0} account is already in use.'.format(provider)
            # raise AuthAlreadyAssociated(backend, msg)
        elif not user:
            user = social.user
    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': False}

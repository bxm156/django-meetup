from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.shortcuts import RequestContext

from DealsNearMe.apps.accounts.forms import CrispyUserProfileForm
from DealsNearMe.apps.accounts.forms import CrispyUserRegistrationForm


@login_required
def overview(request):
    context = RequestContext(request)
    user = request.user
    context.update({
        'first_name': user.first_name,
        'last_name': user.last_name,
        'city': user.city,
    })
    return render_to_response('overview.djhtml', context_instance=context)


@login_required
def edit_profile(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = CrispyUserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            context.update({'submitted': True})
    else:
        form = CrispyUserProfileForm(instance=request.user)
    context.update({'form': form})
    return render_to_response('edit_profile.djhtml', context_instance=context)


def registration(request):
    form = CrispyUserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/login")
    context = RequestContext(request)
    context.update({'form': form})
    return render_to_response('registration.djhtml', context_instance=context)


def logout(request):
    logout_user(request)
    return redirect("/")

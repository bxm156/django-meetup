from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.shortcuts import RequestContext

from DealsNearMe.apps.accounts.forms import CrispyUserProfileForm
from DealsNearMe.apps.accounts.forms import CrispyUserRegistrationForm


@login_required
def overview(request):
    context = RequestContext(request)
    user = request.user
    user_profile = user.get_profile()
    context.update({
        'first_name': user.first_name,
        'last_name': user.last_name,
        'city': user_profile.city,
    })
    return render_to_response('overview.djhtml', context_instance=context)


@login_required
def edit_profile(request):
    user_profile = request.user.get_profile()
    context = RequestContext(request)
    if request.method == 'POST':
        form = CrispyUserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = CrispyUserProfileForm(instance=user_profile)
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

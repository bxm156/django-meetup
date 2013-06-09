from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.shortcuts import RequestContext

from DealsNearMe.apps.accounts.forms import UserRegistrationForm


@login_required
def view_page(request):
    user_profile = request.user.get_profile()


def registration(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/login")
    context = RequestContext(request)
    context.update({'form': form})
    return render_to_response('registration.djhtml', context_instance=context)

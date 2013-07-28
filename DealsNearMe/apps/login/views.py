from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.shortcuts import redirect
from DealsNearMe.apps.login.forms import CrispyAuthenticationForm


def login(request):
    form = CrispyAuthenticationForm(data=request.POST or None)
    if form.is_valid():
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user is not None:
            django_login(request, user)
            return redirect("/account")
    context=RequestContext(request)
    context.update({'form': form})
    return render_to_response('login.djhtml', context_instance=context)

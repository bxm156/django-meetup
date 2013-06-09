from django.shortcuts import render_to_response


def hompage(request):
    return render_to_response('homepage.djhtml')

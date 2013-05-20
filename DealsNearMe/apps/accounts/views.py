from django.contrib.auth.decorators import login_required


@login_required
def view_page(request):
    user_profile = request.user.get_profile()
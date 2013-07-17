def navbar(request):
    user_logged_in = request.user.is_authenticated()
    username = request.user.username if user_logged_in else None

    return {
        'IS_USER_LOGGED_IN': user_logged_in,
        'LOGGED_IN_USERNAME': username,
    }

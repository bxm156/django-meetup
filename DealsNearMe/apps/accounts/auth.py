from django.contrib.auth import get_user_model


class CustomAuth(object):

    def authenticate(self, username=None, password=None):
        try:
            user = get_user_model().objects.get(email=username)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = get_user_model().objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except get_user_model().DoesNotExist:
            return None
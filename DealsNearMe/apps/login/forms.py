from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.helper import FormHelper


class CrispyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

    def __init__(self, request=None, *args, **kwargs):
        super(CrispyAuthenticationForm, self).__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-login'
        self.helper.form_method = 'post'
        self.helper.form_action = '/login/'
        self.helper.form_tag = True

        self.helper.layout = Layout(
                Field('username', label='', placeholder="Username", css_class="input-block-level"),
                Field('password', label='', placeholder="Password", css_class="input-block-level"),
                Submit('submit', 'Sign in', css_class="btn-large")
        )

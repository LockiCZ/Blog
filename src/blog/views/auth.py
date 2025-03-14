from django.contrib.auth import views as auth_views
from django.contrib import messages

from ..forms import LoginForm


class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    form_class = LoginForm


class LogoutView(auth_views.LogoutView):
    http_method_names = ['post', 'get']
    next_page = "/"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, self.request.locals["messages"]["logout_success"])
        return super().post(request, *args, **kwargs)  # by default logout is a post request


class PasswordResetView(auth_views.PasswordResetView):
    pass


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    pass


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    pass


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    pass


class PasswordChangeView(auth_views.PasswordChangeView):
    pass


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    pass

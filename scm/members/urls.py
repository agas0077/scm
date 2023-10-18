# Third Party Library
import django.contrib.auth.views as djviews
from django.urls import path, reverse_lazy
from members.views import sign_up_success

app_name = "members"

urlpatterns = [
    path(
        "login/",
        djviews.LoginView.as_view(template_name="members/login.html"),
        name="login",
    ),
    path("logout/", djviews.LogoutView.as_view(), name="logout"),
    path(
        "password_change/done/",
        djviews.PasswordChangeDoneView.as_view(
            template_name="members/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_change/",
        djviews.PasswordChangeView.as_view(
            template_name="members/password_change_form.html"
        ),
        name="password_change",
    ),
    path(
        "reset/done/",
        djviews.PasswordResetCompleteView.as_view(
            template_name="members/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "reset/<slug:uidb64>/<slug:token>/",
        djviews.PasswordResetConfirmView.as_view(
            template_name="members/password_reset_confirm.html",
            success_url=reverse_lazy("members:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/done/",
        djviews.PasswordResetDoneView.as_view(
            template_name="members/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset/",
        djviews.PasswordResetView.as_view(
            template_name="members/password_reset_form.html",
            email_template_name="members/password_reset_email.html",
            success_url=reverse_lazy("members:password_reset_done"),
        ),
        name="password_reset_form",
    ),
    path("sign_up_success/", sign_up_success, name="sign_up_success"),
]

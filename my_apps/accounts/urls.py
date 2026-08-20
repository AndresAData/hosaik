from django.urls import path

from my_apps.accounts import views

app_name = "accounts"

urlpatterns = [
    path(
        "signup/",
        views.UserRegisterView.as_view(),
        name="signup",
    ),
    path(
        "login/",
        views.UserLoginView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        views.UserLogoutView.as_view(),
        name="logout",
    ),
]

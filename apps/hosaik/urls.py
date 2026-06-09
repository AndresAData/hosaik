from django.urls import path

from apps.hosaik.views import HomeView

app_name = "hosaik"

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
]

from django.urls import path

from my_apps.hosaik import views

app_name = "hosaik"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]

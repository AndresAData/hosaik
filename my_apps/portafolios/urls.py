from django.urls import path

from my_apps.portafolios.views import (
    ProjectContentCreateView,
    ProjectContentUpdateView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectListView,
    ProjectUpdateView,
)

app_name = "portafolio"

urlpatterns = [
    path(
        "",
        ProjectListView.as_view(),
        name="project_list",
    ),
    path(
        "projects/create/",
        ProjectCreateView.as_view(),
        name="project_create",
    ),
    path(
        "projects/<slug:slug>/edit/",
        ProjectUpdateView.as_view(),
        name="project_update",
    ),
    path(
        "projects/<slug:slug>/",
        ProjectDetailView.as_view(),
        name="project_detail",
    ),
    path(
        "projects/<slug:slug>/content/create/",
        ProjectContentCreateView.as_view(),
        name="content_create",
    ),
    path(
        "projects/<slug:slug>/content/<int:pk>/edit/",
        ProjectContentUpdateView.as_view(),
        name="content_edit",
    ),
]

from django.urls import path

from my_apps.portafolios.views import ProjectDetailView, ProjectListView

app_name = "portafolio"

urlpatterns = [
    path(
        "",
        ProjectListView.as_view(),
        name="project_list",
    ),
    path(
        "projects/<slug:slug>/",
        ProjectDetailView.as_view(),
        name="project_detail",
    ),
]

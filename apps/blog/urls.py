from django.urls import path

from apps.blog.views import PostsView

app_name = "blog"

urlpatterns = [
    path("", PostsView.as_view(), name="posts"),
]

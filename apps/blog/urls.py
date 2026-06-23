from django.urls import path

from apps.blog.views import PostDetailView, PostsView

app_name = "blog"

urlpatterns = [
    path("", PostsView.as_view(), name="posts"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post"),
]

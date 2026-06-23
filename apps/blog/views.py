from django.db.models import Prefetch
from django.views.generic import DetailView, ListView

from apps.blog.models import Post, PostContent

# Create your views here.


class PostsView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):

        return (
            Post.objects.filter(status=Post.Status.PUBLISHED)
            .prefetch_related("tags")
            .only(
                "title",
                "slug",
                "description",
                "cover",
                "created_at",
                "reading_time",
                "featured",
                "status",
            )
        )


class PostDetailView(DetailView):
    model = Post

    template_name = "blog/post_detail.html"

    context_object_name = "post"

    slug_field = "slug"

    slug_url_kwarg = "slug"

    def get_queryset(self):

        contents_queryset = PostContent.objects.order_by("order")

        return (
            Post.objects.filter(status=Post.Status.PUBLISHED)
            .select_related("author")
            .prefetch_related(
                "tags",
                Prefetch(
                    "contents",
                    queryset=contents_queryset,
                ),
            )
        )

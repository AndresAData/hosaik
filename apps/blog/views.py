from django.views.generic import ListView

from apps.blog.models import Post

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

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from my_apps.portafolios.forms import ProjectContentForm, ProjectForm, TagForm
from my_apps.portafolios.models import Project, ProjectContent, Tag

# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = "portafolios/projects/list.html"
    context_object_name = "projects"
    paginate_by = 12

    def get_queryset(self):
        return Project.objects.prefetch_related("tags").order_by("-created_at")


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portafolios/projects/detail.html"
    context_object_name = "project"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Project.objects.prefetch_related("tags", "contents")


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "portafolios/projects/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["tag_form"] = TagForm()

        return context

    def get_success_url(self):
        return reverse(
            "portafolio:project_detail",
            kwargs={"slug": self.object.slug},
        )


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "portafolios/projects/update.html"
    context_object_name = "project"

    def get_success_url(self):
        return reverse(
            "portafolio:project_detail",
            kwargs={
                "slug": self.object.slug,
            },
        )


class ProjectContentCreateView(CreateView):
    model = ProjectContent
    form_class = ProjectContentForm
    template_name = "portafolios/content/create.html"

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(
            Project,
            slug=self.kwargs["slug"],
        )

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = self.project

        return context

    def form_valid(self, form):
        form.instance.project = self.project

        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "portafolio:project_detail",
            kwargs={"slug": self.project.slug},
        )


# PROJECT CONTENT MANAGMENT -- DO THIS AFTER FINISHING THE PROJECT CREATION


class ProjectContentUpdateView(UpdateView):
    model = ProjectContent
    form_class = ProjectContentForm
    template_name = "portafolios/content/update.html"
    context_object_name = "content"

    def get_queryset(self):
        return ProjectContent.objects.filter(project__slug=self.kwargs["slug"])

    def get_success_url(self):
        return reverse(
            "portafolio:project_detail",
            kwargs={"slug": self.object.project.slug},
        )


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm

    def form_valid(self, form):
        form.save()

        return redirect(
            self.request.META.get(
                "HTTP_REFERER",
                reverse("portafolio:project_create"),
            )
        )

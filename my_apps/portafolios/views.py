from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from my_apps.portafolios.forms import ProjectContentForm, ProjectForm
from my_apps.portafolios.models import Project, ProjectContent

# Create your views here.


class ProjectListView(ListView):
    template_name = "portafolios/list.html"
    model = Project
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portafolios/detail.html"
    context_object_name = "project"


class ProjectContentUpdateView(UpdateView):
    model = ProjectContent
    form_class = ProjectContentForm
    template_name = "portafolios/content/edit.html"
    context_object_name = "content"

    def get_success_url(self):
        return reverse(
            "portafolio:project_detail",
            kwargs={"slug": self.object.project.slug},
        )


# WORKING ON THIS


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "portafolios/create.html"

    def get_success_url(self):
        return reverse("portafolio:project_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content_form"] = ProjectContentForm()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        content_form = ProjectContentForm(self.request.POST)
        if content_form.is_valid():
            content = content_form.save(commit=False)
            content.project = self.object
            content.save()
        return response


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "portafolios/update.html"

    def get_success_url(self):
        return reverse("portafolio:project_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content_form"] = ProjectContentForm()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        content_form = ProjectContentForm(self.request.POST)
        if content_form.is_valid():
            content = content_form.save(commit=False)
            content.project = self.object
            content.save()
        return response

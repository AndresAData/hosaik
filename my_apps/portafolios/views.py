from django.views.generic import DetailView, ListView

from my_apps.portafolios.models import Project

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

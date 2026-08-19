from django.views.generic import TemplateView

# Create your views here.
from my_apps.portafolios.models import Project


class IndexView(TemplateView):
    template_name = "hosaik/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["projects"] = Project.objects.order_by("-created_at")[:3]

        return context

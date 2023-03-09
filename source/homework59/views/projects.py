from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from homework59.models import Project, Issue

from homework59.forms import ProjectForm


class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetail(DetailView):
    template_name = 'project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['issues'] = Issue.objects.all().exclude(is_deleted=True).filter(project=project.pk)
        return context


class ProjectCreate(CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from homework59.forms import IssueForm
from homework59.models import Issue


class IssueDetail(DetailView):
    template_name = 'issue.html'
    model = Issue


class IssueUpdateView(UpdateView):
    template_name = 'issue_update.html'
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueCreateView(CreateView):
    template_name = 'issue_create.html'
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueDeleteView(DeleteView):
    template_name = 'issue_delete.html'
    model = Issue
    context_object_name = 'issue'
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
    #     return context
    #
    # #
    # def post(self, request, *args, **kwargs):
    #     issue = get_object_or_404(Issue, pk=kwargs['pk'])
    #     issue.type.clear()
    #     issue.delete()
    #     return redirect('index')

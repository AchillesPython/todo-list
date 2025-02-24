from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import redirect, get_object_or_404
from .models import Task, Tag
from .forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all().order_by('is_done', '-created_at')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('list:task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('list:task_list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('list:task_list')


class TaskToggleStatusView(View):

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('list:task_list')


class TagListView(ListView):
    model = Tag
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('list:tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('list:tag_list')


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('list:tag_list')

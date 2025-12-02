from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import redirect, get_object_or_404
from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = context['tasks']
        context['total_tasks'] = qs.count()
        context['completed_tasks'] = qs.filter(completed=True).count()
        return context

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

class TaskCompleteToggle(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.completed = not task.completed
        task.save()
        return redirect('task-list')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'tasks/signup.html'
    success_url = reverse_lazy('login')

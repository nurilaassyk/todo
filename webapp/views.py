from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task
from django.db.models import Q



class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'task'
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = self.search_value
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(status__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET or None)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return self.request.GET.get('search')


class TaskCreateView(CreateView):
    template_name = 'add_task.html'
    form_class = TaskForm

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)
        if form.is_valid():
            task = form.cleaned_data.get('task')
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            executor = form.cleaned_data.get('executor')
            author = request.user
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            Task.objects.create(task=task, description=description, status=status, executor=executor, author=author,
                                start_date=start_date, end_date=end_date)
            return redirect('index')
        return render(request, template_name='add_task.html', context={'form': form})


class TaskDetailView(DetailView):
    template_name = 'task_detail.html'
    model = Task
    context_object_name = 'task'


class TaskEditView(UserPassesTestMixin, UpdateView):
    template_name = 'task_edit.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'task'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('index')


class TaskDeleteView(UserPassesTestMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('delete_photo')

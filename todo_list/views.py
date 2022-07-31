from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import DeadlineForm
from todo_list.models import Tag, Task


def index(requests):
    count_tag = Tag.objects.count()
    count_task = Task.objects.count()

    context = {
        "count_tag": count_tag,
        "count_task": count_task,
    }

    return render(requests, "todo_list/index.html", context=context)


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "todo_list/tags_list.html"


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags-list")


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo_list/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list:tags-list")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo_list/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = DeadlineForm
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.CreateView):
    model = Task
    form_class = DeadlineForm
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_list/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list:index")


def task_compleat(request, pk):
    task_ = Task.objects.get(pk=pk)
    task_.done = False
    task_.save()
    return HttpResponseRedirect(reverse_lazy("todo_list:index"))


def task_undo(request, pk):
    task_ = Task.objects.get(pk=pk)
    task_.done = True
    task_.save()
    return HttpResponseRedirect(reverse_lazy("todo_list:index"))

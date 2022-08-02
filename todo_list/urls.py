from django.urls import path

from todo_list.views import TagsListView, TagsCreateView, TagsDeleteView, TagsUpdateView, TaskCreateView, \
    TaskListView, task_complete, task_undo, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("task/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/compleat", task_complete, name="task-complete"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/undo", task_undo, name="task-undo"),
    path("tag/", TagsListView.as_view(), name="tags-list"),
    path("tag/create", TagsCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update", TagsUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete", TagsDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo_list"

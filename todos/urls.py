from django.urls import path
from . import views

app_name = "todos"
urlpatterns = [
    path("", views.todo_list, name="todo-list"),
    path("create/", views.todo_create, name="todo-create"),
    path("done/<int:todo_id>/", views.todo_done_undone, name="todo-done-undone"),
    path("delete/<int:todo_id>/", views.todo_delete, name="todo-delete"),
]

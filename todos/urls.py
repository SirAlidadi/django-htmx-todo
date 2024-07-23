from django.urls import path
from . import views

app_name = "todos"
urlpatterns = [
    path("", views.todo_list, name="todo-list"),
    path("create/", views.todo_create, name="todo-create")
]

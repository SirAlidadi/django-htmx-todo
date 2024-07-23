from django.shortcuts import render
from todos.forms import TodoForm
from todos.models import Todo


# Create your views here.
def todo_list(request):
    context = {
        'todos': Todo.objects.all(),
        'form': TodoForm()
    }
    return render(request, context=context, template_name="todos/todo-list.html")


def todo_create(request):
    form = TodoForm(data=request.POST)

    if form.is_valid():
        todo = form.save()
        context = {
            'todo': todo
        }
        return render(request, template_name="todos/todo-list.html#todo-list-item", context=context)

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from todos.forms import TodoForm
from todos.models import Todo


# Create your views here.
@require_http_methods(["GET"])
def todo_list(request):
    context = {
        'todos': Todo.objects.all(),
        'form': TodoForm()
    }
    return render(request, context=context, template_name="todos/todo-list.html")


@require_http_methods(["POST"])
def todo_create(request):
    form = TodoForm(data=request.POST)

    if form.is_valid():
        todo = form.save()
        context = {
            'todo': todo
        }
        return render(request, template_name="todos/todo-list.html#todo-list-item", context=context)


@require_http_methods(["POST"])
def todo_done_undone(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.done = not todo.done
    todo.save()

    context = {
        'todo': todo
    }

    return render(request, template_name="todos/todo-list.html#todo-list-item", context=context)


@require_http_methods(["DELETE"])
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    response = HttpResponse(status=204)
    response['HX-Trigger'] = 'todo-delete'
    return response


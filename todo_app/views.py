from django.http import HttpResponse
from django.shortcuts import render

from .models import ToDo


def index(request):
    return render(request, "todo_app/home.html")


def app(request):
    context = {"todos": ToDo.objects.all()}
    return render(request, "todo_app/app.html", context)


def todo_list(request):
    todos = ToDo.objects.all()
    if request.method == "POST":
        todo = ToDo(description=request.POST["description"])
        todo.save()
        newest_todo_id = todo.id
    else:
        newest_todo_id = None
    context = {"todos": todos, "newest_todo_id": newest_todo_id}
    return render(request, "todo_app/app/todo-list.html", context)


def todo(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    if request.method == "DELETE":
        todo.delete()
        return HttpResponse(status=200)
    elif request.method == "POST":
        todo.completed = not todo.completed
        todo.save()
    else:
        return HttpResponse(status=405)
    return render(request, "todo_app/app/todo-item.html", {"todo": todo})


def todo_text(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    if request.method == "POST":
        if description := request.POST["description"]:
            todo.description = description
        todo.save()
        return render(
            request,
            "todo_app/app/todo-text.html",
            {"todo": todo, "editing": False},
        )
    elif request.method == "GET":
        return render(
            request,
            "todo_app/app/todo-text.html",
            {"todo": todo, "editing": True},
        )
    else:
        return HttpResponse(status=405)

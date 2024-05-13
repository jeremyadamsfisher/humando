from django.urls import path

from . import views

app_name = "todo_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("app/", views.app, name="app"),
    path("todo/", views.todo_list, name="todo_list"),
    path("todo/item/<int:todo_id>/", views.todo_text, name="todo_text"),
    path("todo/<int:todo_id>/", views.todo, name="todo"),
]

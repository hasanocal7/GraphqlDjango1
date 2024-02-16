from strawberry_django.auth.utils import get_current_user
from .models import Todo
from strawberry_django import permissions

def get_all_todos(info):
    user = get_current_user(info=info)
    return list(Todo.objects.filter(isDone=False, user=user))

def get_todo(info, id: int):
    user = get_current_user(info=info)
    return Todo.objects.get(id=id, user=user)

def create_todo(info, name: str):
    user = get_current_user(info=info)
    todo = Todo(name=name, user=user)
    todo.save()
    return todo

def update_todo(info, id: int, name: str = None, isDone: bool = None):
    user = get_current_user(info=info)
    todo = Todo.objects.get(id=id, user=user)
    if name is not None: todo.name=name
    if isDone is not None: todo.isDone=isDone
    todo.save()
    return todo

def delete_todo(info, id: int):
    user = get_current_user(info=info)
    todo = Todo.objects.get(id=id, user=user)
    todo.delete()
    return "Todo is deleted"
import strawberry_django
from strawberry import auto
from strawberry.relay import Node
from strawberry_django import NodeInput
from django.contrib.auth.models import User

from .models import Todo

@strawberry_django.type(Todo)
class TodoType(Node):
    name: auto
    isDone: auto
    user: 'UserType'

@strawberry_django.input(Todo)
class TodoInput:
    name: auto

@strawberry_django.partial(Todo)
class TodoInputPartial(NodeInput):
    name: auto
    isDone: auto

@strawberry_django.type(User)
class UserType:
    id: auto
    username: auto
    todos: list[TodoType]

@strawberry_django.input(User)
class UserInput:
    username: auto
    password: auto
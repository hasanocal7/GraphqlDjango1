import strawberry
import strawberry_django
from .types import TodoType, TodoInput, TodoInputPartial
from .resolvers import get_all_todos, get_todo
from strawberry_django import mutations, NodeInput
from .permissions import LoginRequired

@strawberry.type
class Query: 
    todos: list[TodoType] = strawberry_django.field(resolver=get_all_todos, permission_classes=[LoginRequired])
    todo: TodoType = strawberry_django.field(resolver=get_todo, permission_classes=[LoginRequired])

@strawberry.type 
class Mutation:
    create_todo: TodoType = mutations.create(TodoInput, permission_classes=[LoginRequired])
    update_todo: TodoType = mutations.update(TodoInputPartial, permission_classes=[LoginRequired])
    delete_todo: str = mutations.delete(NodeInput, permission_classes=[LoginRequired])
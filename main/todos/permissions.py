import typing
from strawberry.types import Info
from strawberry_django.auth.utils import get_current_user
from strawberry.permission import BasePermission
from .types import TodoType

class LoginRequired(BasePermission):
    message = "You must be logged"

    def has_permission(self, source: TodoType, info: Info, **kwargs: typing.Any) -> bool:
        user = get_current_user(info=info)
        return user.is_authenticated if user else False
    
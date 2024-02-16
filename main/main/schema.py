from todos import schema
import strawberry
from strawberry_django.optimizer import DjangoOptimizerExtension
from strawberry import object_type

class Query(schema.Query): pass

class Mutation(schema.Mutation): pass

schema = strawberry.Schema(query=Query, mutation=Mutation, extensions=[
    DjangoOptimizerExtension
])
import graphene
from .types import Query as SchemeQuery
from .mutations import Mutation as SchemaMutation

class Query(SchemeQuery, graphene.ObjectType):
    pass

class Mutation(SchemaMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
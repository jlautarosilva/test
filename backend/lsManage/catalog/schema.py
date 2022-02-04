import graphene
from .types import Query as SchemeQuery
from .mutations import ProductMutation, AuthMutation

#imports for graphql_auth
from graphql_auth.schema import UserQuery, MeQuery

class Query(UserQuery, SchemeQuery, graphene.ObjectType):
    pass

class Mutation(ProductMutation, AuthMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
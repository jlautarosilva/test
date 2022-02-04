import graphene
from products.models import *
from .types import * 

class CreateProductMutation(graphene.Mutation):
    class Input(object):
        name = graphene.String()
        sku = graphene.String()
        price = graphene.Float()

    name = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, **kwargs):
        sku = kwargs.get('sku','').strip()
        name = kwargs.get('name','').strip()
        price = kwargs.get('price',0)
        
        obj = Product.objects.create(sku=sku, name=name, price=price)
        
        return CreateProductMutation(name=obj)

class Mutation(graphene.AbstractType):
    create_product = CreateProductMutation.Field()

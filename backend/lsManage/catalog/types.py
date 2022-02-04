from typing_extensions import Self
import graphene
from graphene_django.types import DjangoObjectType
from products.models import Product
from graphene_django.filter import DjangoFilterConnectionField

#Product Type definition
class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("sku", "name", "price")

#Graphene query definitions
class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product_by_sku = graphene.Field(ProductType, sku=graphene.String(required=True))

    #List all products in the database
    def resolve_all_products(root, info):
        return Product.objects.all()

    #Get product by SKY and count the anonymus visits
    def resolve_product_by_sku(root, info, sku):
        try:
            product = Product.objects.get(sku = sku)
            if not info.context.user.is_authenticated:
                product.add_visit()
                product.save()
            return product
        except Product.DoesNotExist:
            return None
import graphene
from graphene_django.types import DjangoObjectType
from products.models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("sku", "name", "price")

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product_by_sku = graphene.Field(ProductType, sku=graphene.String(required=True))

    def resolve_all_products(root, info):
        return Product.objects.all()

    def resolve_product_by_sku(root, info, sku):
        try:
            return Product.objects.get(sku=sku)
        except Product.DoesNotExist:
            return None
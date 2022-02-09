from typing_extensions import Self
import graphene
from graphene_django.types import DjangoObjectType
from products.models import Product, Storage, Stock
from graphene_django.filter import DjangoFilterConnectionField

#Para usar graphene_gis
from graphene_gis.converter import gis_converter

#Product Type definition
class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("sku", "name", "price", "storage")

class StorageType(DjangoObjectType):
    class Meta:
        model = Storage
        fields = ("name","location")

class StockType(DjangoObjectType):
    class Meta:
        model = Stock
        fields = ("product","storage","quantity")

#Graphene query definitions
class Query(graphene.ObjectType):
    #Products
    all_products = graphene.List(ProductType)
    product_by_sku = graphene.Field(ProductType, sku=graphene.String(required=True))

    #Storages
    all_storages = graphene.List(StorageType)
    all_stocks = graphene.List(StorageType)

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

    def resolve_all_storages(root, info):
        return Storage.objects.all()

    def resolve_all_stock(root, info):
        return Storage.objects.all()
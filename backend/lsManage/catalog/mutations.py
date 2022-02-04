from email import message
from itertools import product
import graphene
from products.models import *
from .types import *
from graphql_auth import mutations

#Graphene CREATE mutation definition
class CreateProductMutation(graphene.Mutation):
    class Input(object):
        name = graphene.String()
        sku = graphene.String()
        price = graphene.Float()

    name = graphene.Field(ProductType)

    #Define mutation for new product creation using GraphQL
    @staticmethod
    def mutate(root, info, **kwargs):
        if info.context.user.is_authenticated:
            sku = kwargs.get('sku','').strip()
            name = kwargs.get('name','').strip()
            price = kwargs.get('price',0)

            obj = Product.objects.create(sku=sku, name=name, price=price)

            return CreateProductMutation(name=obj)
        else:
            return None

#Graphene UPDATE by ID mutation definition
class UpdateProductMutation(graphene.Mutation):
    class Arguments:
        sku = graphene.String(required=True)
        name = graphene.String(required=True)
        price = graphene.Float()
        id = graphene.ID()

    # The class attributes define the response of the mutation
    product = graphene.Field(ProductType)

    @classmethod
    def mutate(cls, root, info, sku, name, price, id):
        if info.context.user.is_authenticated:
            product = Product.objects.get(pk=id)
            product.sku = sku
            product.name = name
            product.price = price
            product.save()
            return UpdateProductMutation(product=product)
        else:
            None

#Graphene DELETE by ID mutation definition
class DeleteProductMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    id = graphene.ID()
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, id):
        if info.context.user.is_authenticated:
            product = Product.objects.get(pk=id)
            product.delete()
            return cls(id=id, message='deleted')
        else:
            None

#Product mutation class
class ProductMutation(graphene.AbstractType):
    create_product = CreateProductMutation.Field()
    update_product = UpdateProductMutation.Field()
    delete_product = DeleteProductMutation.Field()

#Users mutation class
class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field() # For passwordless registration
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation =  mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()
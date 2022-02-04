
#Test para probar catalogo graphQL
from catalog.schema import schema
from django.test.testcases import TestCase
import graphene

class productsTest(TestCase):
    def testAllProducts(self):
        query = """
            query {
                allProducts {
                    sku
                    name
            }
        }
        """
        result = schema.execute(query)
        assert not result.errors

    def testCreateProductAnonymus(self):
        query = """
            mutation{
              createProduct(
                name:"Juan Valez"
                sku:"CAFE000001"
                price: 5000.00){
                name{
                  name
                }
              }
            }
        """
        result = schema.execute(query)
        assert result.errors

    def testBySKU(self):
        query = """
            query {
              productBySku(sku:"CAFE000001") {
                name
                price
              }
            }
        """
        result = schema.execute(query)
        assert not result.errors
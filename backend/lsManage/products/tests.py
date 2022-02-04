from os import name
from django.test import TestCase
from django.db.models import Avg

from products.models import Product

#Test basico para ver que no han cambiado los tipos de datos
class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(sku="CAFE000001", name="Juan Valez", price=5000.00)
        Product.objects.create(sku="BEER000001", name="Traf", price=2000.00)

    def test_get(self):
        byName = Product.objects.get(name="Juan Valez")
        bySKU = Product.objects.get(sku="BEER000001")
        byPrice = Product.objects.all().aggregate(Avg('price'))
        
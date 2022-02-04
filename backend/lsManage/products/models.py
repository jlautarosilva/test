from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return u"%s %s %s" % (self.name, self.sku, self.price)
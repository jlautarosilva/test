from django.db import models

#Product model
class Product(models.Model):
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    count_nn = models.IntegerField(default=0)

    def __str__(self):
        return u"%s %s %s %s" % (self.id, self.name, self.sku, self.price)

    def add_visit(self):
        self.count_nn = self.count_nn +1
from django.contrib.gis.db import models

#Storage model 
class Storage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.PointField()

    def __str__(self):
        return u"%s %s %s" % (self.id, self.name, self.location)

#Product model
class Product(models.Model):
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    count_nn = models.IntegerField(default=0)
    storage = models.ManyToManyField(Storage, through='Stock')

    def __str__(self):
        return u"%s %s %s %s" % (self.id, self.name, self.sku, self.price)

    def add_visit(self):
        self.count_nn = self.count_nn +1

#Stock of a product for each specific Storage
class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    
    def __str__(self):
        return u"%s %s %s" % (self.product.name, self.storage.name, self.quantity)
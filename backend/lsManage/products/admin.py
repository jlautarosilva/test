from django.contrib.gis import admin
from products.models import Product, Stock, Storage

admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Storage, admin.OSMGeoAdmin)


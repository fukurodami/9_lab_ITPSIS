from django.contrib import admin
from .models import Client, Service, Product, ProductCategory, Production

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Production)
admin.site.register(ProductCategory)

from django.contrib import admin
from gadgets.models import Manufacturer, ProductCategory, Product, Tag

admin.site.register(Manufacturer)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Tag)
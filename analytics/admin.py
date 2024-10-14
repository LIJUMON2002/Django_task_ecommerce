from django.contrib import admin
from .models import Product,Order,OrderItem,Category,Customer,Inventory,Tag

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(Tag)


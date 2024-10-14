from django.utils import timezone
from analytics.models import Category, Product, Customer, Order, OrderItem, Inventory, Tag
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create categories
        electronics = Category.objects.create(name='Electronics')
        clothing = Category.objects.create(name='Clothing')
        books = Category.objects.create(name='Books')

        # Create tags
        tag_sale = Tag.objects.create(name='Sale')
        tag_new = Tag.objects.create(name='New Arrival')

        # Create products
        product1 = Product.objects.create(
            name='Smartphone',
            description='Latest model smartphone with all the features.',
            SKU='SP123',
            price=699.99,
            category=electronics
        )
        product1.tags.add(tag_sale)
        
        product2 = Product.objects.create(
            name='T-Shirt',
            description='Comfortable cotton t-shirt.',
            SKU='TS456',
            price=19.99,
            category=clothing
        )
        product2.tags.add(tag_new)
        
        product3 = Product.objects.create(
            name='Novel Book',
            description='Bestselling novel.',
            SKU='NB789',
            price=14.99,
            category=books
        )

        # Create inventory for products
        Inventory.objects.create(product=product1, quantity=50)
        Inventory.objects.create(product=product2, quantity=20)
        Inventory.objects.create(product=product3, quantity=100)

        # Create customers
        customer1 = Customer.objects.create(
            name='John Doe',
            email='john@example.com',
            country='US'
        )
        
        customer2 = Customer.objects.create(
            name='Jane Smith',
            email='jane@example.com',
            country='UK'
        )

        # Create orders
        order1 = Order.objects.create(
            customer=customer1,
            order_date=timezone.now(),
            status='C',
            total_amount=719.98  # Including tax
        )

        order2 = Order.objects.create(
            customer=customer2,
            order_date=timezone.now(),
            status='C',
            total_amount=34.98  # Including tax
        )

        # Create order items
        OrderItem.objects.create(
            order=order1,
            product=product1,
            quantity=1,
            price_at_time_of_order=699.99
        )
        
        OrderItem.objects.create(
            order=order1,
            product=product2,
            quantity=1,
            price_at_time_of_order=19.99
        )

        OrderItem.objects.create(
            order=order2,
            product=product3,
            quantity=2,
            price_at_time_of_order=14.99
        )

        print("Seed data created successfully!")


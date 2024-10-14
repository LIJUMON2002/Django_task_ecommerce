from django.utils import timezone
from analytics.models import Category, Product, Customer, Order, OrderItem, Inventory, Tag
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create more categories
        office_supplies = Category.objects.create(name='Office Supplies')
        sports = Category.objects.create(name='Sports')

        # Create more tags
        tag_new_arrival = Tag.objects.create(name='New Arrival')
        tag_clearance = Tag.objects.create(name='Clearance')

        # Create more products
        product10 = Product.objects.create(
            name='Notebook',
            description='Spiral-bound notebook for notes and sketches.',
            SKU='NB007',
            price=12.99,
            category=office_supplies
        )
        product10.tags.add(tag_new_arrival)

        product11 = Product.objects.create(
            name='Soccer Ball',
            description='Official size soccer ball for practice and games.',
            SKU='SB008',
            price=29.99,
            category=sports
        )
        product11.tags.add(tag_clearance)

        # Create inventory for new products
        Inventory.objects.create(product=product10, quantity=200)
        Inventory.objects.create(product=product11, quantity=100)

        # Create more customers
        customer9 = Customer.objects.create(
            name='Grace Lee',
            email='grace@example.com',
            country='US'
        )
        
        customer10 = Customer.objects.create(
            name='Henry King',
            email='henry@example.com',
            country='CA'
        )

        # Create more orders
        order9 = Order.objects.create(
            customer=customer9,
            order_date=timezone.now(),
            status='C',
            total_amount=42.98  # Including tax
        )

        order10 = Order.objects.create(
            customer=customer10,
            order_date=timezone.now(),
            status='C',
            total_amount=29.99  # Including tax
        )

        # Create more order items
        OrderItem.objects.create(
            order=order9,
            product=product10,
            quantity=2,
            price_at_time_of_order=12.99
        )
        
        OrderItem.objects.create(
            order=order10,
            product=product11,
            quantity=1,
            price_at_time_of_order=29.99
        )

        print("Fourth batch of additional seed data created successfully!")

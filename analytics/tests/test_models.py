
from django.test import TestCase
from analytics.models import Category, Product, Customer, Order, OrderItem, Inventory
from django.utils import timezone

class ModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            name='Laptop',
            description='A high-performance laptop.',
            SKU='LAP123',
            price=999.99,
            category=self.category
        )
        self.customer = Customer.objects.create(
            name='John Doe',
            email='john.doe@example.com',
            country='US'
        )
        self.order = Order.objects.create(
            customer=self.customer,
            order_date=timezone.now(),
            status='C',
            total_amount=999.99
        )
        self.inventory = Inventory.objects.create(
            product=self.product,
            quantity=10,
            last_restocked_date=timezone.now()
        )

    def test_product_popular(self):
        OrderItem.objects.create(order=self.order, product=self.product, quantity=2, price_at_time_of_order=self.product.price)
        popular_products = Product.objects.popular()
        self.assertEqual(popular_products.first(), self.product)


    def test_calculate_lifetime_value(self):
        new_customer = Customer.objects.create(name='Jane Doe', email='jane.doe@example.com', country='US')
        Order.objects.create(customer=new_customer, order_date=timezone.now(), status='C', total_amount=100.00)
        Order.objects.create(customer=new_customer, order_date=timezone.now(), status='C', total_amount=200.00)
        
        lifetime_value = new_customer.calculate_lifetime_value()
        self.assertEqual(lifetime_value, 300.00)

    def test_order_tax_calculation(self):
        expected_tax = self.order.calculate_tax()  
        self.assertAlmostEqual(expected_tax, 70.00, places=2)

    def test_inventory_restock_alert(self):
        self.inventory.quantity = 3  
        self.inventory.save()
        self.assertEqual(self.inventory.quantity, 3)

    def test_order_item_inventory_update(self):
        initial_quantity = self.inventory.quantity
        order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=2, price_at_time_of_order=self.product.price)
        self.product.refresh_from_db()
        self.assertEqual(self.inventory.quantity, initial_quantity - order_item.quantity)

    from unittest.mock import patch

    @patch('builtins.print') 
    def test_inventory_restock_alert_trigger(self, mock_print):
        self.inventory.quantity = 4 
        self.inventory.save() 
        mock_print.assert_called_once_with(f"Restock alert: {self.product.name} is low on stock!")

    def test_tax_calculation_for_different_countries(self):
        # US Tax
        us_order = Order.objects.create(customer=self.customer, order_date=timezone.now(), status='C', total_amount=100.00)
        self.assertAlmostEqual(us_order.calculate_tax(), 7.00)

        # UK Tax
        uk_customer = Customer.objects.create(name='Alice Smith', email='alice.smith@example.com', country='UK')
        uk_order = Order.objects.create(customer=uk_customer, order_date=timezone.now(), status='C', total_amount=100.00)
        self.assertAlmostEqual(uk_order.calculate_tax(), 20.00)

        # No Tax
        no_tax_customer = Customer.objects.create(name='Bob Brown', email='bob.brown@example.com', country='Other')
        no_tax_order = Order.objects.create(customer=no_tax_customer, order_date=timezone.now(), status='C', total_amount=100.00)
        self.assertAlmostEqual(no_tax_order.calculate_tax(), 0.00)

    def test_customer_lifetime_value_with_no_orders(self):
        new_customer = Customer.objects.create(name='Charlie Green', email='charlie.green@example.com', country='US')
        lifetime_value = new_customer.calculate_lifetime_value()
        self.assertEqual(lifetime_value, 0.00)

    def test_order_status_update(self):
        self.order.status = 'P' 
        self.order.save()
        self.assertEqual(self.order.status, 'P')


from decimal import Decimal
from django.test import TestCase
from analytics.models import Product, Category, Customer, Order, OrderItem, Inventory
from analytics.analytics import SalesAnalytics
from datetime import date, timedelta

class SalesAnalyticsTests(TestCase):
    def setUp(self):
        # Create sample categories
        self.category1 = Category.objects.create(name='Electronics')
        self.category2 = Category.objects.create(name='Clothing')

        # Create sample products
        self.product1 = Product.objects.create(name='Laptop', price=1000.00, category=self.category1)
        self.product2 = Product.objects.create(name='Smartphone', price=500.00, category=self.category1)
        self.product3 = Product.objects.create(name='T-Shirt', price=20.00, category=self.category2)

        # Create inventory for each product
        Inventory.objects.create(product=self.product1, quantity=10)
        Inventory.objects.create(product=self.product2, quantity=10)
        Inventory.objects.create(product=self.product3, quantity=10)

        # Create sample customers
        self.customer1 = Customer.objects.create(name='John Doe', email='john@example.com', country='US')

        # Create orders and order items
        self.order1 = Order.objects.create(customer=self.customer1, order_date=date.today(), total_amount=2000.00)
        self.order_item1 = OrderItem.objects.create(order=self.order1, product=self.product1, quantity=1, price_at_time_of_order=self.product1.price)
        self.order_item2 = OrderItem.objects.create(order=self.order1, product=self.product2, quantity=2, price_at_time_of_order=self.product2.price)

        self.order2 = Order.objects.create(customer=self.customer1, order_date=date.today() - timedelta(days=1), total_amount=20.00)
        self.order_item3 = OrderItem.objects.create(order=self.order2, product=self.product3, quantity=1, price_at_time_of_order=self.product3.price)

    def test_revenue_by_category(self):
        results = SalesAnalytics.revenue_by_category(date.today() - timedelta(days=7), date.today())
        self.assertEqual(len(results), 2)  # Two categories
        self.assertEqual(results[0]['product__category__name'], 'Electronics')
        self.assertEqual(results[0]['total'], Decimal('2000.00')) 

    def test_top_selling_products_by_country(self):
        results = SalesAnalytics.top_selling_products_by_country('US', date.today() - timedelta(days=7), date.today())
        self.assertEqual(len(results), 3)  
        self.assertEqual(results[0].total_sales, 2)

    def test_compute_customer_churn_rate(self):
        churn_rate = SalesAnalytics.compute_customer_churn_rate(date.today() - timedelta(days=30))
        self.assertEqual(churn_rate, 0)  # No churn since we have only one customer

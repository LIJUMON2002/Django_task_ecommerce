from django.test import TestCase
from analytics.models import Product, Category, Customer, Order, OrderItem, Inventory
from analytics.analytics import RecommendationEngine
from datetime import date

class RecommendationEngineTests(TestCase):
    def setUp(self):
        # Create sample categories
        self.category = Category.objects.create(name='Books')

        # Create sample products
        self.product1 = Product.objects.create(name='Book 1', price=15.00, category=self.category)
        self.product2 = Product.objects.create(name='Book 2', price=25.00, category=self.category)

        # Create inventory for each product
        Inventory.objects.create(product=self.product1, quantity=2)
        Inventory.objects.create(product=self.product2, quantity=10)

        # Create sample customers
        self.customer1 = Customer.objects.create(name='Alice', email='alice@example.com', country='US')
        self.customer2 = Customer.objects.create(name='Bob', email='bob@example.com', country='UK')

        # Create orders and order items for Alice
        self.order1 = Order.objects.create(customer=self.customer1, order_date=date.today(), total_amount=15.00)
        self.order_item1 = OrderItem.objects.create(order=self.order1, product=self.product1, quantity=1, price_at_time_of_order=self.product1.price)

        # Create orders and order items for Bob
        self.order2 = Order.objects.create(customer=self.customer2, order_date=date.today(), total_amount=25.00)
        self.order_item2 = OrderItem.objects.create(order=self.order2, product=self.product2, quantity=1, price_at_time_of_order=self.product2.price)

        self.order3 = Order.objects.create(customer=self.customer2, order_date=date.today(), total_amount=15.00)
        self.order_item3 = OrderItem.objects.create(order=self.order3, product=self.product1, quantity=1, price_at_time_of_order=self.product1.price)

    def test_recommend_products_based_on_history(self):
        recommendations = RecommendationEngine.recommend_products_based_on_history(self.customer1)
        self.assertIn(self.product1, recommendations)

    def test_recommend_products_based_on_similar_customers(self):
        recommendations = RecommendationEngine.recommend_products_based_on_similar_customers(self.customer1)
        self.assertIn(self.product2, recommendations)

    def test_recommend_products_based_on_inventory(self):
        recommendations = RecommendationEngine.recommend_products_based_on_inventory()
        self.assertIn(self.product1, recommendations)
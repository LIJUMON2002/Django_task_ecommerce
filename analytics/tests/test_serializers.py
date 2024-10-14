from django.utils import timezone
from django.test import TestCase
from analytics.models import Category, Customer, Inventory, Order, OrderItem, Product
from analytics.serializers import (
    UserRegistrationSerializer,
    ProductSerializer,
    InventorySerializer,
    OrderSerializer,
    OrderItemSerializer,
)

class SerializerTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            name='Laptop',
            description='A high-performance laptop.',
            SKU='LAP123',
            price=999.99,
            category=self.category
        )

        # Use get_or_create to avoid duplicate entry errors
        self.inventory, created = Inventory.objects.get_or_create(
            product=self.product,
            defaults={'quantity': 10}
        )

        self.customer = Customer.objects.create(
            name='John Doe',
            email='john.doe@example.com',
            country='US'
        )
        self.order = Order.objects.create(
            customer=self.customer,
            order_date=timezone.now().date(),
            status='C',
            total_amount=999.99
        )



    def test_user_registration_serializer_valid(self):
        serializer = UserRegistrationSerializer(data={
            'username': 'testuser',
            'password': 'password123',
            'email': 'test@example.com'
        })
        self.assertTrue(serializer.is_valid())

    def test_user_registration_serializer_invalid_email(self):
        serializer = UserRegistrationSerializer(data={
            'username': 'testuser',
            'password': 'password123',
            'email': 'invalid-email'
        })
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_user_registration_serializer_invalid_username(self):
        serializer = UserRegistrationSerializer(data={
            'password': 'password123',
            'email': 'test@example.com'
        })
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

    def test_user_registration_password_hashing(self):
        serializer = UserRegistrationSerializer(data={
            'username': 'testuser',
            'password': 'password123',
            'email': 'test@example.com'
        })
        serializer.is_valid()
        user = serializer.save()
        self.assertNotEqual(user.password, 'password123')  # Ensure password is hashed

    def test_product_serializer(self):
        serializer = ProductSerializer(instance=self.product)
        self.assertEqual(serializer.data['id'], self.product.id)
        self.assertEqual(serializer.data['name'], 'Laptop')
        self.assertEqual(serializer.data['SKU'], 'LAP123')
        self.assertEqual(serializer.data['price'], '999.99')
        self.assertEqual(serializer.data['category'], self.category.id)  # Assuming you want to return category ID

    def test_inventory_serializer(self):
        # Ensure inventory is only created once and test the serializer here
        inventory_data = InventorySerializer(instance=self.inventory).data
        self.assertEqual(inventory_data['product'], self.product.id)
        self.assertEqual(inventory_data['quantity'], 10)

    def test_order_serializer(self):
        serializer = OrderSerializer(instance=self.order)
        self.assertEqual(serializer.data['customer'], self.customer.id)  # Check if customer ID is serialized correctly
        self.assertEqual(serializer.data['total_amount'], '999.99')

    def test_order_item_serializer(self):
        order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=2, price_at_time_of_order=self.product.price)
        serializer = OrderItemSerializer(instance=order_item)
        self.assertEqual(serializer.data['order'], self.order.id)
        self.assertEqual(serializer.data['product'], self.product.id)
        self.assertEqual(serializer.data['quantity'], 2)

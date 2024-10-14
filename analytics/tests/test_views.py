
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
import json
from django.test import TestCase
from analytics.models import Category, Product, Customer, Order, OrderItem, Inventory
from django.utils import timezone
from django.db.models.query import QuerySet


class ViewTests(TestCase):

    # Initial values setup
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.category_electronics = Category.objects.create(name='Electronics')
        self.category_clothing = Category.objects.create(name='Clothing')
        self.category_sleeping = Category.objects.create(name='Sleeping')
        self.category_home_appliances = Category.objects.create(name='Home Appliances')

        self.product_laptop = Product.objects.create(
            name='Laptop',
            description='A high-performance laptop.',
            SKU='LAP123',
            price=999.99,
            category=self.category_electronics
        )
        self.product_shirt = Product.objects.create(
            name='T-Shirt',
            description='A comfortable cotton t-shirt.',
            SKU='TSHIRT123',
            price=19.99,
            category=self.category_clothing
        )
        self.product_bed = Product.objects.create(
            name='Bed',
            description='A comfortable cotton bed.',
            SKU='BED23',
            price=199.99,
            category=self.category_sleeping
        )
        self.product_blender = Product.objects.create(
            name='Blender',
            description='A high-speed blender for smoothies.',
            SKU='BLENDER123',
            price=49.99,
            category=self.category_home_appliances
        )
        self.product_jeans = Product.objects.create(
            name='Jeans',
            description='Stylish denim jeans.',
            SKU='JEANS123',
            price=39.99,
            category=self.category_clothing
        )

        self.customer_john = Customer.objects.create(
            name='John Doe',
            email='john.doe@example.com',
            country='US'
        )
        self.customer_jane = Customer.objects.create(
            name='Jane Smith',
            email='jane.smith@example.com',
            country='UK'
        )
        self.customer_bob = Customer.objects.create(
            name='Bob Brown',
            email='bob.brown@example.com',
            country='US'
        )
        self.customer_anna = Customer.objects.create(
            name='Anna Green',
            email='anna.green@example.com',
            country='AU'
        )

        self.order_john = Order.objects.create(
            customer=self.customer_john,
            order_date=timezone.now().date(),
            status='C',
            total_amount=999.99
        )
        self.order_jane = Order.objects.create(
            customer=self.customer_jane,
            order_date=timezone.now().date(),
            status='C',
            total_amount=39.98
        )
        self.order_bob = Order.objects.create(
            customer=self.customer_bob,
            order_date=timezone.now().date(),
            status='C',
            total_amount=19.99
        )

        self.inventory_laptop = Inventory.objects.create(
            product=self.product_laptop,
            quantity=10,
            last_restocked_date=timezone.now().date()
        )
        self.inventory_shirt = Inventory.objects.create(
            product=self.product_shirt,
            quantity=50,
            last_restocked_date=timezone.now().date()
        )
        self.inventory_bed = Inventory.objects.create(
            product=self.product_bed,
            quantity=1,
            last_restocked_date=timezone.now().date()
        )
        self.inventory_blender = Inventory.objects.create(
            product=self.product_blender,
            quantity=30,
            last_restocked_date=timezone.now().date()
        )
        self.inventory_jeans = Inventory.objects.create(
            product=self.product_jeans,
            quantity=25,
            last_restocked_date=timezone.now().date()
        )

        self.token = RefreshToken.for_user(self.user)


    def set_authentication(self):
        self.token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token.access_token))


    def test_create_order(self):
        self.set_authentication() 
        response = self.client.post(reverse('order-list'), {
            'customer': self.customer_john.id,
            'total_amount': 150.00,
            'status': 'P',
            'order_date': timezone.now().date() 
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_popular_products(self):
        self.set_authentication()  
        OrderItem.objects.create(order=self.order_john, product=self.product_laptop, quantity=5, price_at_time_of_order=self.product_laptop.price)
        OrderItem.objects.create(order=self.order_jane, product=self.product_shirt, quantity=3, price_at_time_of_order=self.product_shirt.price)
        response = self.client.get(reverse('popular_products'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5) 
        self.assertIn('Laptop', [product['name'] for product in response.data])
        self.assertIn('T-Shirt', [product['name'] for product in response.data])
        self.assertIn('Jeans', [product['name'] for product in response.data])
        self.assertIn('Blender', [product['name'] for product in response.data])
        self.assertIn('Bed', [product['name'] for product in response.data])

    def test_customer_lifetime_value(self):
        self.set_authentication() 
        response = self.client.get(reverse('customer_lifetime_value', args=[self.customer_john.id])) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = json.loads(response.content)
        self.assertIn('lifetime_value', response_data)

    def test_create_multiple_orders(self):
        self.set_authentication() 
        response_john = self.client.post(reverse('order-list'), {
            'customer': self.customer_john.id,
            'total_amount': 150.00,
            'status': 'P',
            'order_date': timezone.now().date() 
        })
        response_jane = self.client.post(reverse('order-list'), {
            'customer': self.customer_jane.id, 
            'total_amount': 250.00,
            'status': 'P',
            'order_date': timezone.now().date() 
        })
        self.assertEqual(response_john.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_jane.status_code, status.HTTP_201_CREATED)

    def test_list_customers(self):
        self.set_authentication() 
        response = self.client.get(reverse('customer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)


    def test_get_popular_products_with_multiple_categories(self):
        self.set_authentication()  
        OrderItem.objects.create(order=self.order_john, product=self.product_laptop, quantity=5, price_at_time_of_order=self.product_laptop.price)
        OrderItem.objects.create(order=self.order_jane, product=self.product_shirt, quantity=3, price_at_time_of_order=self.product_shirt.price)
        OrderItem.objects.create(order=self.order_bob, product=self.product_jeans, quantity=2, price_at_time_of_order=self.product_jeans.price)

        response = self.client.get(reverse('popular_products'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertIn('Laptop', [product['name'] for product in response.data])
        self.assertIn('T-Shirt', [product['name'] for product in response.data])
        self.assertIn('Jeans', [product['name'] for product in response.data])
        self.assertIn('Blender', [product['name'] for product in response.data])
        self.assertIn('Bed', [product['name'] for product in response.data])



    def test_customer_lifetime_value_multiple_orders(self):
        self.set_authentication() 
        response = self.client.get(reverse('customer_lifetime_value', args=[self.customer_john.id]))  
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = json.loads(response.content)
        self.assertIn('lifetime_value', response_data)
        self.assertEqual(response_data['lifetime_value'], '999.99')

    def test_inventory_management(self):
        self.set_authentication() 
        response = self.client.get(reverse('inventory-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

        response_laptop = self.client.get(reverse('inventory-detail', args=[self.inventory_laptop.id]))
        self.assertEqual(response_laptop.status_code, status.HTTP_200_OK)
        self.assertEqual(response_laptop.data['quantity'], 10)


    # Report generation view
    def test_monthly_sales_report(self):
        response = self.client.get(reverse('monthly_sales_report', args=[10, 2024]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Content-Disposition', response.headers)
    

    # sales analytics views
    def test_revenue_by_category(self):
        self.set_authentication()
        response = self.client.get(reverse('revenue_by_category', args=['2023-01-01', '2023-12-31']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, QuerySet) 

    
    def test_top_selling_products_by_country(self):
        self.set_authentication()

        OrderItem.objects.create(order=self.order_john, product=self.product_laptop, quantity=5, price_at_time_of_order=self.product_laptop.price)
        OrderItem.objects.create(order=self.order_jane, product=self.product_shirt, quantity=3, price_at_time_of_order=self.product_shirt.price)

        response = self.client.get(reverse('top_selling_products', args=['US', '2023-01-01', '2024-12-31']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_names = [product['name'] for product in response.data]
        self.assertIn('Laptop', product_names)

    def test_customer_churn_rate(self):
        self.set_authentication()
        period = '2024-09-01'

        Customer.objects.create(name='Churned Customer1', email='churned1@example.com', country='US')
        Order.objects.create(customer=self.customer_jane,order_date='2023-10-01',status='C',total_amount=50.00)
        Customer.objects.create(name='Churned Customer2', email='churned2@example.com', country='UK')
        Order.objects.create(customer=self.customer_jane,order_date='2023-10-01',status='C',total_amount=50.00)

        response = self.client.get(reverse('customer_churn_rate', args=[period]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertIn('churn_rate', response_data)
        expected_churn_rate = 16.666666666666664 
        self.assertAlmostEqual(response_data['churn_rate'], expected_churn_rate, delta=0.1)



    #recommendation views

    def test_recommend_products(self):
        self.set_authentication()
        response = self.client.get(reverse('recommend_products', args=[self.customer_john.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, QuerySet)


    def test_recommend_products_based_on_history(self):
        self.set_authentication()
        
        order = Order.objects.create(customer=self.customer_john, total_amount=100.00, status='C')
        OrderItem.objects.create(
            order=order,
            product=self.product_laptop,
            quantity=1,
            price_at_time_of_order=self.product_laptop.price
        )

        response = self.client.get(reverse('recommend_products_based_on_history', args=[self.customer_john.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertIn('id', response.data[0]) 
        self.assertIn('name', response.data[0]) 


    def test_recommend_products_based_on_similar_customers(self):
        self.set_authentication()
        Order.objects.create(customer=self.customer_bob, total_amount=100.00, status='C')
        OrderItem.objects.create(
            order=self.order_bob,
            product=self.product_laptop,
            quantity=1,
            price_at_time_of_order=self.product_laptop.price
        )
        
        response = self.client.get(reverse('recommend_products_based_on_similar_customers', args=[self.customer_john.id]))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        if response.data:
            self.assertIn('id', response.data[0])
            self.assertIn('name', response.data[0])


    def test_recommend_products_based_on_inventory(self):
        self.set_authentication()
        response = self.client.get(reverse('recommend_based_on_inventory'))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', response.data[0])
        self.assertIn('name', response.data[0])


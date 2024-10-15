from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductManager(models.Manager):
    #finding top products by checking orderitem quantity
    def popular(self):
        return self.annotate(total_sales=Sum('orderitem__quantity')).order_by('-total_sales')

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    SKU = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ProductManager()

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Calculate lifetime value by adding total-amount of all orders
    def calculate_lifetime_value(self):
        orders = self.order_set.all()
        return sum(order.total_amount for order in orders)

class Order(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('R', 'Returned'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #calculate tax according to tax-rate
    def calculate_tax(self):
        tax_rates = {
            'US': 0.07,
            'UK': 0.2
        }
        return self.total_amount * tax_rates.get(self.customer.country, 0)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_time_of_order = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Signal for OrderItem table, updating the Inventory Table
@receiver(post_save, sender=OrderItem)
def update_inventory(sender, instance, created, **kwargs):
    if created:
        inventory = instance.product.inventory
        inventory.quantity -= instance.quantity
        inventory.save()

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    last_restocked_date = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.quantity < 5:  
            self.trigger_restock_alert()
        super().save(*args, **kwargs)

    # Print alert when quantity become lessthan 5
    def trigger_restock_alert(self):
        print(f"Restock alert: {self.product.name} is low on stock!")

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

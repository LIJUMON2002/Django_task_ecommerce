from django.db.models import Sum,F
from .models import OrderItem, Product, Customer

class SalesAnalytics:
    @staticmethod
    def revenue_by_category(start_date, end_date):
        return (
            OrderItem.objects
            .filter(order__order_date__range=(start_date, end_date))  # Filter orders by date range
            .values('product__category__name')  # Group by category name
            .annotate(total=Sum(F('quantity') * F('price_at_time_of_order')))  # Calculate total revenue
        )


    @staticmethod
    def top_selling_products_by_country(country, start_date, end_date):
        return (
            Product.objects.filter(orderitem__order__customer__country=country, orderitem__order__order_date__range=(start_date, end_date))
            .annotate(total_sales=Sum('orderitem__quantity'))
            .order_by('-total_sales')
        )


    @staticmethod
    def compute_customer_churn_rate(period):
        total_customers = Customer.objects.count()
        churned_customers = Customer.objects.filter(order__order_date__lt=period).distinct().count()
        churn_rate = (churned_customers / total_customers) * 100 if total_customers > 0 else 0
        return churn_rate



class RecommendationEngine:
    @staticmethod
    def recommend_products(customer):
        # Get all orders for the customer
        orders = customer.order_set.all()
        purchased_product_ids = OrderItem.objects.filter(order__in=orders).values_list('product_id', flat=True)

        # Get products that similar customers have purchased
        similar_customers = Customer.objects.exclude(id=customer.id).filter(order__orderitem__product__in=purchased_product_ids)
        similar_product_ids = OrderItem.objects.filter(order__customer__in=similar_customers).exclude(product_id__in=purchased_product_ids).values_list('product_id', flat=True)

        # Current inventory levels
        inventory_products = Product.objects.filter(inventory__quantity__gt=0)

        # Final recommendations: products that are in inventory and recommended
        recommended_products = Product.objects.filter(id__in=similar_product_ids).intersection(inventory_products)
        return recommended_products

    @staticmethod
    def recommend_products_based_on_history(customer):
        """Suggest products based on customer's order history."""
        # Get all orders for the customer
        orders = customer.order_set.all()
        purchased_product_ids = OrderItem.objects.filter(order__in=orders).values_list('product_id', flat=True)
        return Product.objects.filter(id__in=purchased_product_ids)
    
    @staticmethod
    def recommend_products_based_on_similar_customers(customer):
        purchased_product_ids = RecommendationEngine.recommend_products_based_on_history(customer).values_list('id', flat=True)
        similar_customers = Customer.objects.exclude(id=customer.id).filter(order__orderitem__product__in=purchased_product_ids)
        similar_product_ids = OrderItem.objects.filter(order__customer__in=similar_customers)\
                                                .exclude(product_id__in=purchased_product_ids)\
                                                .values_list('product_id', flat=True)
        return Product.objects.filter(id__in=similar_product_ids)
    
    @staticmethod
    def recommend_products_based_on_inventory():
        return Product.objects.filter(inventory__quantity__lt=5)

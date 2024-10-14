from rest_framework import viewsets,generics,status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import OrderItem, Product, Customer, Order, Inventory
from .serializers import OrderItemSerializer, ProductSerializer, CustomerSerializer, OrderSerializer, InventorySerializer, UserRegistrationSerializer
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponse,JsonResponse
from .reports import export_monthly_sales_report
import os
from rest_framework.response import Response
from rest_framework.views import APIView
from .analytics import SalesAnalytics, RecommendationEngine
from django.utils import timezone
from rest_framework import serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]


class MonthlySalesReportView(View):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, month, year):
        try:
            file_path = export_monthly_sales_report(month,year)
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(),content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
                return response
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)



class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny] 

class PopularProductsView(generics.ListAPIView):
    queryset = Product.objects.popular() 
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated] 

class CustomerLifetimeValueSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    lifetime_value = serializers.DecimalField(max_digits=10, decimal_places=2)

class CustomerLifetimeValueView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated] 

    serializer_class = CustomerLifetimeValueSerializer

    def get(self, request, *args, **kwargs):
        customer = self.get_object() 
        lifetime_value = customer.calculate_lifetime_value()
        return JsonResponse({"customer_id": customer.id, "lifetime_value": lifetime_value})
    


#SALES VIEWS
class RevenueByCategoryView(APIView):
    def get(self, request, start_date, end_date):
        revenue_data = SalesAnalytics.revenue_by_category(start_date, end_date)
        return Response(revenue_data, status=status.HTTP_200_OK)


class TopSellingProductsByCountryView(APIView):
    def get(self, request, country, start_date, end_date):
        top_selling_products = SalesAnalytics.top_selling_products_by_country(country, start_date, end_date)
        serializer = ProductSerializer(top_selling_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerChurnRateView(APIView):
    def get(self, request, period):
        churn_rate = SalesAnalytics.compute_customer_churn_rate(period)
        return Response({"churn_rate": churn_rate}, status=status.HTTP_200_OK)


#RECOMMENDATION VIEWS
class RecommendProductsView(APIView):
    def get(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            recommended_products = RecommendationEngine.recommend_products(customer)
            return Response(recommended_products.values('id', 'name'), status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)


class RecommendProductsBasedOnHistoryView(APIView):
    def get(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            recommended_products = RecommendationEngine.recommend_products_based_on_history(customer)
            return Response(recommended_products.values('id', 'name'), status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)


class RecommendProductsBasedOnSimilarCustomersView(APIView):
    def get(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            recommended_products = RecommendationEngine.recommend_products_based_on_similar_customers(customer)
            return Response(recommended_products.values('id', 'name'), status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)


class RecommendProductsBasedOnInventoryView(APIView):
    def get(self, request):
        recommended_products = RecommendationEngine.recommend_products_based_on_inventory()
        return Response(recommended_products.values('id', 'name'), status=status.HTTP_200_OK)

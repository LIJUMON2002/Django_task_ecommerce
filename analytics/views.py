from rest_framework import viewsets,generics,status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import OrderItem, Product, Customer, Order, Inventory
from .serializers import OrderItemSerializer, ProductSerializer, CustomerSerializer, OrderSerializer, InventorySerializer, UserRegistrationSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from .reports import export_monthly_sales_report
import os
from rest_framework.response import Response
from rest_framework.views import APIView
from .analytics import SalesAnalytics, RecommendationEngine
from rest_framework import serializers

# Models crud operations views
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



# Sales Report view with month and year provided
class MonthlySalesReportView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        month = request.query_params.get('month')
        year = request.query_params.get('year')
        if month is None or year is None:
            return JsonResponse({"error": "Month and year are required."}, status=400)
        try:
            file_path = export_monthly_sales_report(month,year)
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(),content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
                return response
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)



# User Registration View
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny] 


# Popular Product View
class PopularProductsView(generics.ListAPIView):
    queryset = Product.objects.popular() 
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated] 


# Customer lifetime value serializer
class CustomerLifetimeValueSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    lifetime_value = serializers.DecimalField(max_digits=10, decimal_places=2)

# Customer lifetime value View
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
    def get(self, request ):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if end_date is None or end_date is None:
            return JsonResponse({"error": "start_date and end_date are required."}, status=400)
        
        revenue_data = SalesAnalytics.revenue_by_category(start_date, end_date)
        return Response(revenue_data, status=status.HTTP_200_OK)


class TopSellingProductsByCountryView(APIView):
    def get(self, request):
        country = request.query_params.get('country')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if start_date is None or end_date is None or country is None:
            return JsonResponse({"error": "start_date and end_date and country are required."}, status=400)
        top_selling_products = SalesAnalytics.top_selling_products_by_country(country, start_date, end_date)
        serializer = ProductSerializer(top_selling_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerChurnRateView(APIView):
    def get(self, request):
        period = request.query_params.get('period')
        churn_rate = SalesAnalytics.compute_customer_churn_rate(period)
        return Response({"churn_rate": churn_rate}, status=status.HTTP_200_OK)


#RECOMMENDATION VIEWS

class RecommendProducts(APIView):
    def get(self, request, customer_id):
        type = request.query_params.get('type')
        try:
            customer = Customer.objects.get(id=customer_id)
            if type is None:
                    recommended_products = RecommendationEngine.recommend_products(customer)
                    return Response(recommended_products.values('id', 'name'), status=status.HTTP_200_OK)
            if type == "based on history":
                    recommended_products = RecommendationEngine.recommend_products_based_on_history(customer)
                    return Response(recommended_products.values('id', 'name'), status=status.HTTP_200_OK)
            elif type == "based on similar customer":
                    recommended_products = RecommendationEngine.recommend_products_based_on_similar_customers(customer)
                    return Response(recommended_products.values('id', 'name'), status=status.HTTP_200_OK)
            elif type == "based on inventory":
                recommended_products = RecommendationEngine.recommend_products_based_on_inventory()
                return Response(recommended_products.values('id', 'name'), status=status.HTTP_200_OK)
            
            else:
                return Response({"error": "Invalid type specified."},status=status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)
            

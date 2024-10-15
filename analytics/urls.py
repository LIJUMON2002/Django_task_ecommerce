from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import OrderItemViewSet, PopularProductsView, ProductViewSet, CustomerViewSet, OrderViewSet, InventoryViewSet, RecommendProducts, RevenueByCategoryView, TopSellingProductsByCountryView
from .views import UserRegistrationView, MonthlySalesReportView, CustomerChurnRateView, CustomerLifetimeValueView

router = DefaultRouter()

# Models CRUD operation urls
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'inventories', InventoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

 
    # finding top products based on orderitem quantity
    path('top-products/', PopularProductsView.as_view(), name='popular_products'),

    # lifetime value
    path('customers/lifetime_value/<int:pk>/', CustomerLifetimeValueView.as_view(), name='customer_lifetime_value'),

    # URL to generate SALES REPORT with month and year specified
    path('sales-report/', MonthlySalesReportView.as_view(), name='monthly_sales_report'),
    
    # Sales Analytics
    path('sales/revenue_by_category/', RevenueByCategoryView.as_view(), name='revenue_by_category'),
    path('sales/top_selling_products/', TopSellingProductsByCountryView.as_view(), name='top_selling_products'),
    path('sales/churn_rate/', CustomerChurnRateView.as_view(), name='customer_churn_rate'),
    
    #Recommendations
    path('recommend_products/<int:customer_id>/', RecommendProducts.as_view(), name='recommend_products'),
    # if no type specified it will return the recommendation based on history, similar customers and inventory
    # here types can be "based on history", "based on similar customers", "based on inventory"


    #User registration, access token and refresh token generation 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),

]

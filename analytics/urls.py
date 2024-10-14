from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomerChurnRateView, CustomerLifetimeValueView, OrderItemViewSet, PopularProductsView, ProductViewSet, CustomerViewSet, OrderViewSet, InventoryViewSet, RecommendProductsBasedOnHistoryView, RecommendProductsBasedOnInventoryView, RecommendProductsBasedOnSimilarCustomersView, RecommendProductsView, RevenueByCategoryView, TopSellingProductsByCountryView
from .views import UserRegistrationView
from .views import MonthlySalesReportView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'inventories', InventoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),

    path('reports/monthly_sales/<int:month>/<int:year>/', MonthlySalesReportView.as_view(), name='monthly_sales_report'),

    path('top-products/', PopularProductsView.as_view(), name='popular_products'),
    path('customers/<int:pk>/lifetime_value/', CustomerLifetimeValueView.as_view(), name='customer_lifetime_value'),

    path('sales/revenue_by_category/<str:start_date>/<str:end_date>/', RevenueByCategoryView.as_view(), name='revenue_by_category'),
    path('sales/top_selling_products/<str:country>/<str:start_date>/<str:end_date>/', TopSellingProductsByCountryView.as_view(), name='top_selling_products'),
    path('sales/churn_rate/<str:period>/', CustomerChurnRateView.as_view(), name='customer_churn_rate'),
    
    path('recommend_products/<int:customer_id>/', RecommendProductsView.as_view(), name='recommend_products'),
    path('recommend_products/history/<int:customer_id>/', RecommendProductsBasedOnHistoryView.as_view(), name='recommend_products_based_on_history'),
    path('recommend_products/similar/<int:customer_id>/', RecommendProductsBasedOnSimilarCustomersView.as_view(), name='recommend_products_based_on_similar_customers'),
    path('recommend_products/inventory/', RecommendProductsBasedOnInventoryView.as_view(), name='recommend_based_on_inventory'),   
]

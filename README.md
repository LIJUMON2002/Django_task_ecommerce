# E-Commerce Analytics Platform

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd e_commerce_analytics
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

7. Access the API at `http://localhost:8000/api/`


## API Endpoints

Product: /products/
Customer: /customers/
Order: /orders/
OrderItem: /order-items/
Inventory: /inventories/
Sales: 
    /sales/churn_rate/{period}/
    /sales/revenue_by_category/{start_date}/{end_date}/
    /sales/top_selling_products/{country}/{start_date}/{end_date}/
Recommend Products: 
    /recommend_products/history/{customer_id}/
    /recommend_products/inventory/
    /recommend_products/similar/{customer_id}/
    /recommend_products/{customer_id}/

## Key Design Decisions

- **Data Modeling:** Used interconnected models to capture the relationships between products, customers, and orders.
- **Custom Managers & Signals:** Implemented custom managers for frequently used queries and signals for real-time inventory updates.
- **Business Logic:** Separated analytics and recommendation logic for better organization and testing.
- **REST API:** Utilized Django REST Framework with JWT authentication for secure API access.
- **Excel Export:** Leveraged `openpyxl` for generating Excel reports.


## Author

Liju Mon A P
Associate Engineer
Innovature Software Labs
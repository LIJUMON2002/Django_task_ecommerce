import openpyxl
from django.db.models import Sum, F
from .models import Order, OrderItem, Inventory

def export_monthly_sales_report(month, year):
    # Create a new Excel workbook and select the active worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Monthly Sales Report"

    # Append header row to the worksheet
    ws.append(["Product", "Quantity", "Price", "Total Sales", "Remaining Quantity"])

    # Filter orders based on the specified month and year
    orders = Order.objects.filter(order_date__month=month, order_date__year=year)

    # Aggregate sales data from OrderItem for the filtered orders
    sales_data = (
        OrderItem.objects.filter(order__in=orders)
        .values('product__name', 'product__price')
        .annotate(
            total_quantity=Sum('quantity'),
            total_sales=Sum(F('quantity') * F('price_at_time_of_order'))
        )
    )

    inventory_data = Inventory.objects.all().values('product__name', 'quantity')
    inventory_dict = {item['product__name']: item['quantity'] for item in inventory_data}

    # Iterate over the sales data to populate the worksheet
    for data in sales_data:
        product_name = data['product__name']
        total_quantity = data['total_quantity']
        price = data['product__price']
        total_sales = data['total_sales']

        # Get the remaining quantity from inventory for the product
        remaining_quantity = inventory_dict.get(product_name, 0)

        # Append the sales data for the product to the worksheet
        ws.append([product_name, total_quantity, price, total_sales, remaining_quantity])

    # # Define the file path for saving the Excel report
    file_path = f"monthly_sales_{month}_{year}.xlsx"
    wb.save(file_path)
    return file_path

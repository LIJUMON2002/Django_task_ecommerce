import openpyxl
from django.db.models import Sum, F
from .models import Order, OrderItem, Inventory

def export_monthly_sales_report(month, year):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Monthly Sales Report"

    ws.append(["Product", "Quantity", "Price", "Total Sales", "Remaining Quantity"])

    orders = Order.objects.filter(order_date__month=month, order_date__year=year)

    sales_data = (
        OrderItem.objects.filter(order__in=orders)
        .values('product__name', 'product__price')
        .annotate(
            total_quantity=Sum('quantity'),
            total_sales=Sum(F('quantity') * F('price_at_time_of_order'))
        )
    )

    for data in sales_data:
        product_name = data['product__name']
        total_quantity = data['total_quantity']
        price = data['product__price']
        total_sales = data['total_sales']

        remaining_quantity = Inventory.objects.filter(product__name=product_name).values_list('quantity', flat=True).first() or 0

        ws.append([product_name, total_quantity, price, total_sales, remaining_quantity])

    file_path = f"monthly_sales_{month}_{year}.xlsx"
    wb.save(file_path)
    return file_path

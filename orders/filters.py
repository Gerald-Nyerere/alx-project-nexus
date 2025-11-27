import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    user_email = django_filters.CharFilter(field_name="user__email", lookup_expr="icontains")
    order_number = django_filters.CharFilter(field_name="order_number", lookup_expr="icontains")
    start_date = django_filters.DateTimeFilter(field_name="order_date", lookup_expr="gte")
    end_date = django_filters.DateTimeFilter(field_name="order_date", lookup_expr="lte")

    # Amount range
    min_total = django_filters.NumberFilter(field_name="total_amount", lookup_expr="gte")
    max_total = django_filters.NumberFilter(field_name="total_amount", lookup_expr="lte")

    class Meta:
        model = Order
        fields = ["user_email", "order_number", "start_date", "end_date", "min_total", "max_total",]

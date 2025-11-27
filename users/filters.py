import django_filters
from .models import User

class UserFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(field_name="email", lookup_expr="icontains")

    username = django_filters.CharFilter(field_name="username", lookup_expr="icontains")
    roles = django_filters.CharFilter(field_name="roles", lookup_expr="iexact")
    is_active = django_filters.BooleanFilter(field_name="is_active")

    # Registration date range
    created_after = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    created_before = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = User
        fields = ["email", "username", "roles", "is_active", "created_after", "created_before",]

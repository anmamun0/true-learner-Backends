from django_filters import FilterSet
import django_filters 
from .models import studentHistory
class studentHistoryFilter(FilterSet):
    user = django_filters.CharFilter(field_name='user',lookup_expr='exact')
    class Meta:
        model = studentHistory
        fields = ['user']
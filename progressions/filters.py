import django_filters
from django_filters import FilterSet

from .models import Progres

class ProgressFilter(FilterSet):
    student = django_filters.NumberFilter(field_name='student',lookup_expr='exact')
    course = django_filters.NumberFilter(field_name='course',lookup_expr='exact')
    class Meta:
        model = Progres
        fields = ['student','course']

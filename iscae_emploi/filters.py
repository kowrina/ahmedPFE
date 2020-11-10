import django_filters
from django_filters import DateFilter
from .models import *

class SeanceFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date")

    class Meta:
        model = Seance
        fields = '__all__'
        exclude = ['date']

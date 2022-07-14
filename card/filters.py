import django_filters
from .models import *

class CardFilter(django_filters.FilterSet):
    class Meta:
        model = Card
        fields = '__all__'
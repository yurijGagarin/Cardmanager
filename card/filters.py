from datetime import datetime

import django_filters

from . import forms
from .models import *
from django_filters import DateFilter


class CardFilter(django_filters.FilterSet):
    release_date_from = django_filters.DateTimeFilter(
        field_name='release_date',
        label='Released From',
        lookup_expr='gte',
        widget=forms.DateTimePicker(
            options={
                'useCurrent': False,
                'collapse': False,
                'maxDate': str(datetime.now()),

            },
            attrs={
                'append': 'fa fa-calendar',
                'id': 'datepicker1',
                'icon_toggle': True,
            }
        ),
    )
    release_date_to = django_filters.DateTimeFilter(
        field_name='release_date',
        label='Released To',
        lookup_expr='lte',
        widget=forms.DateTimePicker(
            options={
                'useCurrent': False,
                'collapse': False,
                'maxDate': str(datetime.now()),

            },
            attrs={
                'append': 'fa fa-calendar',
                'id': 'datepicker2',
                'icon_toggle': True,
            }
        ),
    )
    end_date_from = django_filters.DateTimeFilter(
        field_name='end_date',
        label='End date From',
        lookup_expr='gte',
        widget=forms.DateTimePicker(
            options={
                'useCurrent': False,
                'collapse': False,
                'maxDate': str(datetime.now()),

            },
            attrs={
                'append': 'fa fa-calendar',
                'id': 'datepicker3',
                'icon_toggle': True,
            }
        ),
    )
    end_date_to = django_filters.DateTimeFilter(
        field_name='end_date',
        label='End date To',
        lookup_expr='lte',
        widget=forms.DateTimePicker(
            options={
                'useCurrent': False,
                'collapse': False,
                'maxDate': str(datetime.now()),

            },
            attrs={
                'append': 'fa fa-calendar',
                'id': 'datepicker4',
                'icon_toggle': True,
            }
        ),
    )

    class Meta:
        model = Card
        fields = '__all__'
        exclude = ['release_date', 'end_date', 'cvv', 'money_on_card']

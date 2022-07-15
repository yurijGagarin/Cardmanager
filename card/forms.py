from datetime import date, timedelta

from django import forms
from tempus_dominus.widgets import DateTimePicker

TTLs = [
    (1, 'month'),
    (6, 'six months'),
    (12, 'year'),
]

STATUSES = [
    ('activated', 'Activated'),
    ('deactivated', 'Deactivated'),
]

maxdate = date.today() + timedelta(1)


class GeneratorForm(forms.Form):
    serial_number = forms.IntegerField(label='Serial Number', required=True)
    amount_to_generate = forms.IntegerField(label='Amount to Generate', required=True)
    released = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
                'maxDate': str(maxdate),

            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )

    ttl = forms.IntegerField(label='Choose desired expire date', widget=forms.Select(choices=TTLs))


class CardEditForm(forms.Form):
    card_status = forms.CharField(label='Card Status', widget=forms.Select(choices=STATUSES))

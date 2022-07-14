from django import forms
TTLs = [
    (1, 'month'),
    (6, 'six months'),
    (12, 'year'),
    ]


class GeneratorForm(forms.Form):
    serial_number = forms.IntegerField(label='serial number', required=True)
    amount_to_generate = forms.IntegerField(label='amount to generate', required=True)
    ttl = forms.IntegerField(label='Choose desired expire date', widget=forms.Select(choices=TTLs))

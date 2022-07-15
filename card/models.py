from datetime import datetime

from django.db import models


class Card(models.Model):
    serial_number = models.IntegerField('Serial Number')
    card_number = models.BigIntegerField('Card Number')
    release_date = models.DateTimeField('Release Date')
    exp_date = models.DateTimeField('Expire Date')
    cvv = models.IntegerField('CVV')
    balance = models.FloatField('Balance')
    card_status = models.CharField('Card Status', default="activated", max_length=25)

    @property
    def is_expired(self):
        return self.exp_date.replace(tzinfo=None) < datetime.utcnow()

    @property
    def status(self):
        if self.is_expired:
            return 'expired'
        return self.card_status

    def __str__(self):
        return str(self.card_number)


class CardTransaction(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    date = models.DateTimeField('Date', auto_now=True)
    amount = models.FloatField('Amount')
